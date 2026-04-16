export const GAME_SOURCE_H = `// blackjack_manager.h
#ifndef __INC_METIN2_BLACKJACK_MANAGER_H__
#define __INC_METIN2_BLACKJACK_MANAGER_H__

#include <vector>
#include <map>
#include <random>
#include <algorithm>

struct TBlackjackGame
{
    long long betAmount;
    std::vector<int> deck;
    std::vector<int> playerHand;
    std::vector<int> dealerHand;
    bool isActive;

    TBlackjackGame() : betAmount(0), isActive(false) {}
};

class CBlackjackManager : public singleton<CBlackjackManager>
{
    public:
        CBlackjackManager();
        virtual ~CBlackjackManager();

        void InitializeGame(LPCHARACTER ch, long long betAmount);
        void ActionHit(LPCHARACTER ch);
        void ActionStand(LPCHARACTER ch);
        
    private:
        void EndGame(LPCHARACTER ch, bool isWin, bool isDraw = false);
        int CalculateScore(const std::vector<int>& hand);
        std::vector<int> CreateDeck();
        int DrawCard(std::vector<int>& deck);
        void SendGamePacket(LPCHARACTER ch);

        std::map<DWORD, TBlackjackGame> m_mapGames;
};

#endif
`;

export const GAME_SOURCE_CPP = `// blackjack_manager.cpp
#include "stdafx.h"
#include "blackjack_manager.h"
#include "char.h"
#include "utils.h"
#include "packet.h"

CBlackjackManager::CBlackjackManager() {}
CBlackjackManager::~CBlackjackManager() {}

void CBlackjackManager::InitializeGame(LPCHARACTER ch, long long betAmount)
{
    if (!ch) return;
    DWORD pid = ch->GetPlayerID();

    if (m_mapGames.find(pid) != m_mapGames.end()) {
        ch->ChatPacket(CHAT_TYPE_INFO, "Zaten aktif bir oyununuz var.");
        return;
    }

    if (ch->GetGold() < betAmount) {
        ch->ChatPacket(CHAT_TYPE_INFO, "Yeterli Yang'ınız yok.");
        return;
    }

    ch->PointChange(POINT_GOLD, -betAmount);

    TBlackjackGame game;
    game.betAmount = betAmount;
    game.deck = CreateDeck();
    std::shuffle(game.deck.begin(), game.deck.end(), std::random_device());
    game.isActive = true;

    // İlk dağıtım
    game.playerHand.push_back(DrawCard(game.deck));
    game.dealerHand.push_back(DrawCard(game.deck));
    game.playerHand.push_back(DrawCard(game.deck));
    game.dealerHand.push_back(DrawCard(game.deck));

    m_mapGames[pid] = game;
    SendGamePacket(ch);
}

void CBlackjackManager::ActionHit(LPCHARACTER ch)
{
    auto it = m_mapGames.find(ch->GetPlayerID());
    if (it == m_mapGames.end()) return;

    TBlackjackGame& game = it->second;
    game.playerHand.push_back(DrawCard(game.deck));

    if (CalculateScore(game.playerHand) > 21)
        EndGame(ch, false);
    else
        SendGamePacket(ch);
}

void CBlackjackManager::ActionStand(LPCHARACTER ch)
{
    auto it = m_mapGames.find(ch->GetPlayerID());
    if (it == m_mapGames.end()) return;

    TBlackjackGame& game = it->second;
    
    while (CalculateScore(game.dealerHand) < 17)
        game.dealerHand.push_back(DrawCard(game.deck));

    int pScore = CalculateScore(game.playerHand);
    int dScore = CalculateScore(game.dealerHand);

    if (dScore > 21 || pScore > dScore)
        EndGame(ch, true);
    else if (pScore == dScore)
        EndGame(ch, true, true);
    else
        EndGame(ch, false);
}

void CBlackjackManager::EndGame(LPCHARACTER ch, bool isWin, bool isDraw)
{
    auto it = m_mapGames.find(ch->GetPlayerID());
    if (it == m_mapGames.end()) return;

    if (isDraw) ch->PointChange(POINT_GOLD, it->second.betAmount);
    else if (isWin) ch->PointChange(POINT_GOLD, it->second.betAmount * 2);

    m_mapGames.erase(it);
    // Client'a oyun bitti paketi gönder
}

int CBlackjackManager::CalculateScore(const std::vector<int>& hand)
{
    int score = 0, aces = 0;
    for (int card : hand) {
        int val = (card % 13) + 1;
        if (val > 10) val = 10;
        if (val == 1) aces++;
        score += val;
    }
    while (score <= 11 && aces > 0) { score += 10; aces--; }
    return score;
}

std::vector<int> CBlackjackManager::CreateDeck() {
    std::vector<int> deck;
    for (int i = 0; i < 52; ++i) deck.push_back(i);
    return deck;
}

int CBlackjackManager::DrawCard(std::vector<int>& deck) {
    int card = deck.back();
    deck.pop_back();
    return card;
}

void CBlackjackManager::SendGamePacket(LPCHARACTER ch) {
    // Burada binary paket veya ChatPacket ile JSON formatında veri gönderebilirsiniz.
}
`;

export const PYTHON_SCRIPT = `# uiBlackjack.py
import ui
import net
import chat

class BlackjackWindow(ui.BoardWithTitleBar):
    def __init__(self):
        ui.BoardWithTitleBar.__init__(self)
        self.__LoadWindow()

    def __LoadWindow(self):
        self.SetSize(400, 300)
        self.SetTitleName("Blackjack")
        self.AddFlag("movable")
        self.AddFlag("float")
        self.CenterWindow()

        self.hitBtn = ui.Button()
        self.hitBtn.SetParent(self)
        self.hitBtn.SetPosition(100, 200)
        self.hitBtn.SetUpVisual("d:/ymir work/ui/public/middle_button_01.sub")
        self.hitBtn.SetOverVisual("d:/ymir work/ui/public/middle_button_02.sub")
        self.hitBtn.SetDownVisual("d:/ymir work/ui/public/middle_button_03.sub")
        self.hitBtn.SetText("Kart Çek")
        self.hitBtn.SetEvent(lambda: net.SendChatPacket("/blackjack hit"))
        self.hitBtn.Show()

        self.standBtn = ui.Button()
        self.standBtn.SetParent(self)
        self.standBtn.SetPosition(200, 200)
        self.standBtn.SetUpVisual("d:/ymir work/ui/public/middle_button_01.sub")
        self.standBtn.SetOverVisual("d:/ymir work/ui/public/middle_button_02.sub")
        self.standBtn.SetDownVisual("d:/ymir work/ui/public/middle_button_03.sub")
        self.standBtn.SetText("Dur")
        self.standBtn.SetEvent(lambda: net.SendChatPacket("/blackjack stand"))
        self.standBtn.Show()

    def Close(self):
        self.Hide()

    def OnPressEscapeKey(self):
        self.Close()
        return True
`;
