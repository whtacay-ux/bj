#ifndef __INC_ITJA_BLACKJACK_MANAGER_H__
#define __INC_ITJA_BLACKJACK_MANAGER_H__

#ifdef ITJA_BLACKJACK_SYSTEM
#include <vector>
#include <map>
#include <random>

enum EBlackjackSubHeaders
{
	BLACKJACK_SUBHEADER_GC_OPEN,
	BLACKJACK_SUBHEADER_GC_UPDATE,
	BLACKJACK_SUBHEADER_GC_RESULT,
	BLACKJACK_SUBHEADER_GC_CLOSE,

	BLACKJACK_SUBHEADER_CG_BET,
	BLACKJACK_SUBHEADER_CG_HIT,
	BLACKJACK_SUBHEADER_CG_STAND,
	BLACKJACK_SUBHEADER_CG_CLOSE,
	BLACKJACK_SUBHEADER_CG_DOUBLE,
	BLACKJACK_SUBHEADER_CG_SPLIT,
	BLACKJACK_SUBHEADER_CG_INSURANCE,
	BLACKJACK_SUBHEADER_CG_SURRENDER,
};

enum EBlackjackState
{
	BLACKJACK_STATE_WAITING_BET,
	BLACKJACK_STATE_PLAYING,
	BLACKJACK_STATE_FINISHED,
};

enum EBlackjackResult
{
	BLACKJACK_RESULT_NONE,
	BLACKJACK_RESULT_WIN,
	BLACKJACK_RESULT_LOSE,
	BLACKJACK_RESULT_DRAW,
	BLACKJACK_RESULT_BLACKJACK,
	BLACKJACK_RESULT_BUST,
	BLACKJACK_RESULT_SURRENDERED,
};

struct TBlackjackGame
{
	long long llBet;
	long long llInsuranceBet;
	BYTE bState;
	std::vector<BYTE> vecPlayerCards;
	std::vector<BYTE> vecDealerCards;
	BYTE bResult;

	// Split
	bool bHasSplit;
	std::vector<BYTE> vecPlayerCardsHand2;
	long long llBetHand2;
	BYTE bCurrentHand;

	TBlackjackGame() : llBet(0), llInsuranceBet(0), bState(BLACKJACK_STATE_WAITING_BET), 
		bResult(BLACKJACK_RESULT_NONE), bHasSplit(false), llBetHand2(0), bCurrentHand(0) {}
};

class CBlackjackManager : public singleton<CBlackjackManager>
{
public:
	CBlackjackManager();
	virtual ~CBlackjackManager();

	void OpenBoard(LPCHARACTER ch);
	void CloseBoard(LPCHARACTER ch);
	
	void Bet(LPCHARACTER ch, long long llAmount);
	void Hit(LPCHARACTER ch);
	void Stand(LPCHARACTER ch);
	void DoubleDown(LPCHARACTER ch);
	void Split(LPCHARACTER ch);
	void Insurance(LPCHARACTER ch);
	void Surrender(LPCHARACTER ch);
	void NewGame(LPCHARACTER ch);

private:
	void SendUpdatePacket(LPCHARACTER ch);
	void SendResultPacket(LPCHARACTER ch, BYTE bResult);
	
	BYTE DrawCard();
	BYTE GetHandValue(const std::vector<BYTE>& vecCards);
	bool IsBlackjack(const std::vector<BYTE>& vecCards);
	BYTE GetCardValue(BYTE bCard);
	
	std::map<DWORD, TBlackjackGame> m_mapGames;
};

#endif
#endif
