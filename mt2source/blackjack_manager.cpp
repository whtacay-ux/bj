#include "stdafx.h"
#ifdef ITJA_BLACKJACK_SYSTEM
#include "blackjack_manager.h"
#include "char.h"
#include "desc.h"
#include "packet.h"
#include "utils.h"
#include "config.h"

static CBlackjackManager s_manager;

CBlackjackManager::CBlackjackManager()
{
}

CBlackjackManager::~CBlackjackManager()
{
}

void CBlackjackManager::OpenBoard(LPCHARACTER ch)
{
	if (!ch) return;

	if (m_mapGames.find(ch->GetPlayerID()) != m_mapGames.end())
	{
		CloseBoard(ch);
	}

	TBlackjackGame& game = m_mapGames[ch->GetPlayerID()];
	game.bState = BLACKJACK_STATE_WAITING_BET;
	game.llBet = 0;
	game.vecPlayerCards.clear();
	game.vecDealerCards.clear();
	game.bResult = BLACKJACK_RESULT_NONE;

	/*
	TPacketGCBlackjack pack;
	pack.header = HEADER_GC_BLACKJACK;
	pack.subheader = BLACKJACK_SUBHEADER_GC_OPEN;
	ch->GetDesc()->Packet(&pack, sizeof(pack));
	*/
	ch->ChatPacket(CHAT_TYPE_COMMAND, "blackjack_open");
}

void CBlackjackManager::CloseBoard(LPCHARACTER ch)
{
	if (!ch) return;

	auto it = m_mapGames.find(ch->GetPlayerID());
	if (it != m_mapGames.end())
	{
		// If closing while playing, player loses the bet
		if (it->second.bState == BLACKJACK_STATE_PLAYING)
		{
			// Already taken from gold at Bet()
		}
		m_mapGames.erase(it);
	}

	/*
	TPacketGCBlackjack pack;
	pack.header = HEADER_GC_BLACKJACK;
	pack.subheader = BLACKJACK_SUBHEADER_GC_CLOSE;
	ch->GetDesc()->Packet(&pack, sizeof(pack));
	*/
	ch->ChatPacket(CHAT_TYPE_COMMAND, "blackjack_close");
}

void CBlackjackManager::Bet(LPCHARACTER ch, long long llAmount)
{
	if (!ch) return;

	auto it = m_mapGames.find(ch->GetPlayerID());
	if (it == m_mapGames.end() || it->second.bState != BLACKJACK_STATE_WAITING_BET)
		return;

	if (llAmount <= 0)
	{
		ch->ChatPacket(CHAT_TYPE_INFO, "Gecersiz bahis miktari.");
		return;
	}

	if (ch->GetGold() < llAmount)
	{
		ch->ChatPacket(CHAT_TYPE_INFO, "Yetersiz Yang.");
		return;
	}

	ch->PointChange(POINT_GOLD, -llAmount);
	
	TBlackjackGame& game = it->second;
	game.llBet = llAmount;
	game.bState = BLACKJACK_STATE_PLAYING;

	// Initial deal
	game.vecPlayerCards.push_back(DrawCard());
	game.vecDealerCards.push_back(DrawCard());
	game.vecPlayerCards.push_back(DrawCard());
	game.vecDealerCards.push_back(DrawCard());

	if (IsBlackjack(game.vecPlayerCards))
	{
		Stand(ch);
		return;
	}

	SendUpdatePacket(ch);
}

void CBlackjackManager::Hit(LPCHARACTER ch)
{
	if (!ch) return;

	auto it = m_mapGames.find(ch->GetPlayerID());
	if (it == m_mapGames.end() || it->second.bState != BLACKJACK_STATE_PLAYING)
		return;

	TBlackjackGame& game = it->second;
	
	std::vector<BYTE>& vecTargetHand = (game.bCurrentHand == 0) ? game.vecPlayerCards : game.vecPlayerCardsHand2;
	
	// Split Ace restriction: Only one card if split aces
	if (game.bHasSplit)
	{
		BYTE bRank1 = (game.vecPlayerCards[0] - 1) % 13 + 1;
		BYTE bRank2 = (game.vecPlayerCardsHand2[0] - 1) % 13 + 1;
		if (bRank1 == 1 && bRank2 == 1)
		{
			ch->ChatPacket(CHAT_TYPE_INFO, "Split Aslara sadece bir kart cekebilirsiniz.");
			return;
		}
	}

	vecTargetHand.push_back(DrawCard());

	BYTE bVal = GetHandValue(vecTargetHand);
	if (bVal >= 21)
	{
		Stand(ch);
	}
	else
	{
		SendUpdatePacket(ch);
	}
}

void CBlackjackManager::Stand(LPCHARACTER ch)
{
	if (!ch) return;

	auto it = m_mapGames.find(ch->GetPlayerID());
	if (it == m_mapGames.end() || it->second.bState != BLACKJACK_STATE_PLAYING)
		return;

	TBlackjackGame& game = it->second;

	if (game.bHasSplit && game.bCurrentHand == 0)
	{
		game.bCurrentHand = 1;
		SendUpdatePacket(ch);
		
		// If hand 2 is already 21 (split with ace and drawn 10), it might need to stand automatically
		if (GetHandValue(game.vecPlayerCardsHand2) >= 21)
			Stand(ch);
			
		return;
	}

	game.bState = BLACKJACK_STATE_FINISHED;

	// Dealer plays
	while (GetHandValue(game.vecDealerCards) < 17)
	{
		game.vecDealerCards.push_back(DrawCard());
	}

	BYTE bDealerVal = GetHandValue(game.vecDealerCards);
	bool bDealerBJ = IsBlackjack(game.vecDealerCards);

	// Insurance payout
	if (game.llInsuranceBet > 0 && bDealerBJ)
	{
		ch->PointChange(POINT_GOLD, game.llInsuranceBet * 3); // 2:1 payout + original insurance bet
		ch->ChatPacket(CHAT_TYPE_INFO, "Sigorta bahsi kazandi!");
	}

	auto ProcessResult = [&](std::vector<BYTE>& vecHand, long long llHandBet) {
		BYTE bPlayerVal = GetHandValue(vecHand);
		BYTE bHandResult = BLACKJACK_RESULT_NONE;

		if (IsBlackjack(vecHand))
		{
			if (bDealerBJ)
			{
				bHandResult = BLACKJACK_RESULT_DRAW;
				ch->PointChange(POINT_GOLD, llHandBet);
			}
			else
			{
				bHandResult = BLACKJACK_RESULT_BLACKJACK;
				ch->PointChange(POINT_GOLD, llHandBet * 2.5); // 3:2 payout (original bet + 1.5 profit)
			}
		}
		else if (bPlayerVal > 21)
		{
			bHandResult = BLACKJACK_RESULT_BUST;
		}
		else if (bDealerVal > 21 || bPlayerVal > bDealerVal)
		{
			bHandResult = BLACKJACK_RESULT_WIN;
			ch->PointChange(POINT_GOLD, llHandBet * 2);
		}
		else if (bPlayerVal == bDealerVal)
		{
			bHandResult = BLACKJACK_RESULT_DRAW;
			ch->PointChange(POINT_GOLD, llHandBet);
		}
		else
		{
			bHandResult = BLACKJACK_RESULT_LOSE;
		}
		return bHandResult;
	};

	game.bResult = ProcessResult(game.vecPlayerCards, game.llBet);
	if (game.bHasSplit)
	{
		// In a split game, bResult for the packet might be tricky, usually send the main result or separate?
		// For now let's just send the main result, maybe the client handles split results differently.
		// We could send both results if we extend the packet.
		ProcessResult(game.vecPlayerCardsHand2, game.llBetHand2);
	}

	SendResultPacket(ch, game.bResult);
}

void CBlackjackManager::SendUpdatePacket(LPCHARACTER ch)
{
	if (!ch) return;

	auto it = m_mapGames.find(ch->GetPlayerID());
	if (it == m_mapGames.end()) return;

	TBlackjackGame& game = it->second;

	std::string strPlayerCards = "";
	for (size_t i = 0; i < game.vecPlayerCards.size(); ++i)
	{
		strPlayerCards += std::to_string(game.vecPlayerCards[i]);
		if (i < game.vecPlayerCards.size() - 1) strPlayerCards += ",";
	}
	if (strPlayerCards.empty()) strPlayerCards = "0";

	std::string strDealerCards = "";
	if (game.bState == BLACKJACK_STATE_PLAYING)
	{
		// Only show first card during play
		if (!game.vecDealerCards.empty())
			strDealerCards = std::to_string(game.vecDealerCards[0]);
		else
			strDealerCards = "0";
	}
	else
	{
		for (size_t i = 0; i < game.vecDealerCards.size(); ++i)
		{
			strDealerCards += std::to_string(game.vecDealerCards[i]);
			if (i < game.vecDealerCards.size() - 1) strDealerCards += ",";
		}
		if (strDealerCards.empty()) strDealerCards = "0";
	}

	ch->ChatPacket(CHAT_TYPE_COMMAND, "blackjack_update %lld %d %d %d %s %s", 
		game.llBet, 
		GetHandValue(game.vecPlayerCards), 
		(game.bState == BLACKJACK_STATE_PLAYING && !game.vecDealerCards.empty()) ? GetCardValue(game.vecDealerCards[0]) : GetHandValue(game.vecDealerCards),
		game.bState,
		strPlayerCards.c_str(),
		strDealerCards.c_str()
	);
}

void CBlackjackManager::SendResultPacket(LPCHARACTER ch, BYTE bResult)
{
	if (!ch) return;

	auto it = m_mapGames.find(ch->GetPlayerID());
	if (it == m_mapGames.end()) return;

	TBlackjackGame& game = it->second;

	std::string strDealerCards = "";
	for (size_t i = 0; i < game.vecDealerCards.size(); ++i)
	{
		strDealerCards += std::to_string(game.vecDealerCards[i]);
		if (i < game.vecDealerCards.size() - 1) strDealerCards += ",";
	}
	if (strDealerCards.empty()) strDealerCards = "0";

	ch->ChatPacket(CHAT_TYPE_COMMAND, "blackjack_result %d %d %d %s", 
		bResult, 
		GetHandValue(game.vecPlayerCards), 
		GetHandValue(game.vecDealerCards),
		strDealerCards.c_str()
	);
}

void CBlackjackManager::NewGame(LPCHARACTER ch)
{
	if (!ch) return;
	
	auto it = m_mapGames.find(ch->GetPlayerID());
	if (it == m_mapGames.end()) return;
	
	TBlackjackGame& game = it->second;
	if (game.bState != BLACKJACK_STATE_FINISHED) return;
	
	game.bState = BLACKJACK_STATE_WAITING_BET;
	game.llBet = 0;
	game.llInsuranceBet = 0;
	game.vecPlayerCards.clear();
	game.vecDealerCards.clear();
	game.bResult = BLACKJACK_RESULT_NONE;
	game.bHasSplit = false;
	game.vecPlayerCardsHand2.clear();
	game.llBetHand2 = 0;
	game.bCurrentHand = 0;
	
	SendUpdatePacket(ch);
}

void CBlackjackManager::DoubleDown(LPCHARACTER ch)
{
	if (!ch) return;

	auto it = m_mapGames.find(ch->GetPlayerID());
	if (it == m_mapGames.end() || it->second.bState != BLACKJACK_STATE_PLAYING)
		return;

	TBlackjackGame& game = it->second;
	
	std::vector<BYTE>& vecTargetHand = (game.bCurrentHand == 0) ? game.vecPlayerCards : game.vecPlayerCardsHand2;
	long long& llTargetBet = (game.bCurrentHand == 0) ? game.llBet : game.llBetHand2;

	if (vecTargetHand.size() != 2) return;

	if (ch->GetGold() < llTargetBet)
	{
		ch->ChatPacket(CHAT_TYPE_INFO, "Yetersiz Yang.");
		return;
	}

	ch->PointChange(POINT_GOLD, -llTargetBet);
	llTargetBet *= 2;

	// Draw exactly one card
	vecTargetHand.push_back(DrawCard());
	
	Stand(ch);
}

void CBlackjackManager::Split(LPCHARACTER ch)
{
	if (!ch) return;

	auto it = m_mapGames.find(ch->GetPlayerID());
	if (it == m_mapGames.end() || it->second.bState != BLACKJACK_STATE_PLAYING || it->second.bHasSplit)
		return;

	TBlackjackGame& game = it->second;

	if (game.vecPlayerCards.size() != 2) return;

	// Check if card values are the same
	if (GetCardValue(game.vecPlayerCards[0]) != GetCardValue(game.vecPlayerCards[1]))
	{
		ch->ChatPacket(CHAT_TYPE_INFO, "Sadece ayni degerdeki kartlari bolebilirsin.");
		return;
	}

	if (ch->GetGold() < game.llBet)
	{
		ch->ChatPacket(CHAT_TYPE_INFO, "Yetersiz Yang.");
		return;
	}

	ch->PointChange(POINT_GOLD, -game.llBet);
	
	game.bHasSplit = true;
	game.llBetHand2 = game.llBet;
	
	// Create second hand
	game.vecPlayerCardsHand2.push_back(game.vecPlayerCards[1]);
	game.vecPlayerCards.pop_back();

	// Draw new cards for each hand
	game.vecPlayerCards.push_back(DrawCard());
	game.vecPlayerCardsHand2.push_back(DrawCard());

	SendUpdatePacket(ch);
}

void CBlackjackManager::Insurance(LPCHARACTER ch)
{
	if (!ch) return;

	auto it = m_mapGames.find(ch->GetPlayerID());
	if (it == m_mapGames.end() || it->second.bState != BLACKJACK_STATE_PLAYING)
		return;

	TBlackjackGame& game = it->second;

	// Only if dealer's first card is an Ace
	BYTE bDealerUpCardRank = (game.vecDealerCards[0] - 1) % 13 + 1;
	if (bDealerUpCardRank != 1) return;

	long long llInsuranceCost = game.llBet / 2;
	if (ch->GetGold() < llInsuranceCost) return;

	ch->PointChange(POINT_GOLD, -llInsuranceCost);
	game.llInsuranceBet = llInsuranceCost;

	ch->ChatPacket(CHAT_TYPE_INFO, "Sigorta bahsi yapildi.");
	SendUpdatePacket(ch);
}

void CBlackjackManager::Surrender(LPCHARACTER ch)
{
	if (!ch) return;

	auto it = m_mapGames.find(ch->GetPlayerID());
	if (it == m_mapGames.end() || it->second.bState != BLACKJACK_STATE_PLAYING || it->second.vecPlayerCards.size() != 2)
		return;

	TBlackjackGame& game = it->second;
	
	long long llRefund = game.llBet / 2;
	ch->PointChange(POINT_GOLD, llRefund);
	
	game.bState = BLACKJACK_STATE_FINISHED;
	SendResultPacket(ch, BLACKJACK_RESULT_SURRENDERED);
}

BYTE CBlackjackManager::GetCardValue(BYTE bCard)
{
	BYTE bRank = (bCard - 1) % 13 + 1;
	if (bRank >= 10) return 10;
	if (bRank == 1) return 11; // Ace handled as 11 initially in GetHandValue logic
	return bRank;
}

BYTE CBlackjackManager::DrawCard()
{
	// 1-52: 1-13 Spades, 14-26 Hearts, 27-39 Diamonds, 40-52 Clubs
	return (number(1, 52));
}

BYTE CBlackjackManager::GetHandValue(const std::vector<BYTE>& vecCards)
{
	BYTE bTotal = 0;
	BYTE bAces = 0;

	for (BYTE bCard : vecCards)
	{
		BYTE bRank = (bCard - 1) % 13 + 1;
		if (bRank == 1)
		{
			bAces++;
			bTotal += 11;
		}
		else if (bRank >= 10)
		{
			bTotal += 10;
		}
		else
		{
			bTotal += bRank;
		}
	}

	while (bTotal > 21 && bAces > 0)
	{
		bTotal -= 10;
		bAces--;
	}

	return bTotal;
}

bool CBlackjackManager::IsBlackjack(const std::vector<BYTE>& vecCards)
{
	if (vecCards.size() != 2) return false;
	return GetHandValue(vecCards) == 21;
}

#endif
