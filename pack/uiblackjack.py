import ui
import net
import chat
import player
import app
import localeInfo

class BlackjackWindow(ui.ScriptWindow):
	STATE_WAITING_BET = 0
	STATE_PLAYING = 1
	STATE_FINISHED = 2

	CARD_SUITS = ["Maça", "Kupa", "Karo", "Sinek"]
	CARD_RANKS = ["As", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Vale", "Kız", "Papaz"]

	def __init__(self):
		ui.ScriptWindow.__init__(self)
		self.isLoaded = False

	def __del__(self):
		ui.ScriptWindow.__del__(self)

	def LoadWindow(self):
		if self.isLoaded:
			return
		
		self.isLoaded = True
		
		try:
			pyScrLoader = ui.PythonScriptLoader()
			pyScrLoader.LoadScriptFile(self, "UIScript/blackjackwindow.py")
		except:
			import exception
			exception.Abort("BlackjackWindow.LoadWindow.LoadObject")

		try:
			self.board = self.GetChild("board")
			self.titleBar = self.GetChild("TitleBar")
			
			self.betInput = self.GetChild("BetInput")
			self.betBtn = self.GetChild("BetButton")
			self.clearBetBtn = self.GetChild("ClearBetButton")
			self.newGameBtn = self.GetChild("NewGameButton")
			
			self.hitBtn = self.GetChild("HitButton")
			self.standBtn = self.GetChild("StandButton")
			self.splitBtn = self.GetChild("SplitButton")
			self.doubleBtn = self.GetChild("DoubleButton")
			self.insuranceBtn = self.GetChild("InsuranceButton")
			self.surrenderBtn = self.GetChild("SurrenderButton")

			self.playerScore = self.GetChild("PlayerScoreValue")
			self.dealerScore = self.GetChild("DealerScoreValue")

			self.playerCardTexts = []
			for i in range(5):
				self.playerCardTexts.append(self.GetChild("PlayerCardValue_%d" % i))
				
			self.dealerCardTexts = []
			for i in range(5):
				self.dealerCardTexts.append(self.GetChild("DealerCardValue_%d" % i))

			self.titleBar.SetCloseEvent(ui.__mem_func__(self.Close))
			self.betBtn.SetEvent(ui.__mem_func__(self.__OnBet))
			self.clearBetBtn.SetEvent(ui.__mem_func__(self.__OnClearBet))
			self.newGameBtn.SetEvent(ui.__mem_func__(self.__OnNewGame))
			
			self.hitBtn.SetEvent(ui.__mem_func__(self.__OnHit))
			self.standBtn.SetEvent(ui.__mem_func__(self.__OnStand))
			self.splitBtn.SetEvent(ui.__mem_func__(self.__OnSplit))
			self.doubleBtn.SetEvent(ui.__mem_func__(self.__OnDouble))
			self.insuranceBtn.SetEvent(ui.__mem_func__(self.__OnInsurance))
			self.surrenderBtn.SetEvent(ui.__mem_func__(self.__OnSurrender))
			
			self.__ResetUI()
			
		except:
			import exception
			exception.Abort("BlackjackWindow.LoadWindow.BindObject")

	def Close(self):
		net.SendChatPacket("/blackjack close")
		self.Hide()

	def Open(self):
		self.LoadWindow()
		self.Show()
		self.SetTop()
		self.__ResetUI()

	def __ResetUI(self):
		self.playerScore.SetText("0")
		self.dealerScore.SetText("0")
		for t in self.playerCardTexts: t.SetText("")
		for t in self.dealerCardTexts: t.SetText("")
		self.__SetButtonState(self.STATE_WAITING_BET)

	def __SetButtonState(self, state):
		if state == self.STATE_WAITING_BET:
			self.betBtn.Enable()
			self.clearBetBtn.Enable()
			self.newGameBtn.Disable()
			self.hitBtn.Disable()
			self.standBtn.Disable()
			self.doubleBtn.Disable()
			self.splitBtn.Disable()
			self.insuranceBtn.Disable()
			self.surrenderBtn.Disable()
		elif state == self.STATE_PLAYING:
			self.betBtn.Disable()
			self.clearBetBtn.Disable()
			self.newGameBtn.Disable()
			self.hitBtn.Enable()
			self.standBtn.Enable()
			self.doubleBtn.Enable()
			self.splitBtn.Enable()
			self.insuranceBtn.Enable()
			self.surrenderBtn.Enable()
		elif state == self.STATE_FINISHED:
			self.betBtn.Disable()
			self.clearBetBtn.Disable()
			self.newGameBtn.Enable()
			self.hitBtn.Disable()
			self.standBtn.Disable()
			self.doubleBtn.Disable()
			self.splitBtn.Disable()
			self.insuranceBtn.Disable()
			self.surrenderBtn.Disable()

	def __OnBet(self):
		amount = self.betInput.GetText()
		if not amount.isdigit():
			return
		net.SendChatPacket("/blackjack bet " + amount)

	def __OnClearBet(self):
		self.betInput.SetText("0")

	def __OnNewGame(self):
		net.SendChatPacket("/blackjack newgame")

	def __OnHit(self):
		net.SendChatPacket("/blackjack hit")

	def __OnStand(self):
		net.SendChatPacket("/blackjack stand")

	def __OnSplit(self):
		net.SendChatPacket("/blackjack split")

	def __OnDouble(self):
		net.SendChatPacket("/blackjack double")

	def __OnInsurance(self):
		net.SendChatPacket("/blackjack insurance")

	def __OnSurrender(self):
		net.SendChatPacket("/blackjack surrender")

	def GetCardName(self, cardId):
		try:
			cid = int(cardId)
			if cid == 0: return "?"
			suit = (cid - 1) / 13
			rank = (cid - 1) % 13
			return "%s %s" % (self.CARD_SUITS[suit], self.CARD_RANKS[rank])
		except:
			return "?"

	def UpdateGame(self, bet, pScore, dScore, state, pCards, dCards):
		try:
			self.playerScore.SetText(str(pScore))
			self.dealerScore.SetText(str(dScore))
			
			nState = int(state)
			self.__SetButtonState(nState)
			
			# Update cards
			p_list = pCards.split(",")
			d_list = dCards.split(",")
			
			for i in range(5):
				if i < len(p_list) and p_list[i] and p_list[i] != "0":
					self.playerCardTexts[i].SetText(self.GetCardName(p_list[i]))
				else:
					self.playerCardTexts[i].SetText("")
					
				if i < len(d_list) and d_list[i] and d_list[i] != "0":
					self.dealerCardTexts[i].SetText(self.GetCardName(d_list[i]))
				else:
					if i == 1 and nState == self.STATE_PLAYING:
						self.dealerCardTexts[i].SetText("?")
					else:
						self.dealerCardTexts[i].SetText("")
		except:
			import exception
			exception.LogException()

	def ShowResult(self, result, pScore, dScore, dCards):
		try:
			self.playerScore.SetText(str(pScore))
			self.dealerScore.SetText(str(dScore))
			self.__SetButtonState(self.STATE_FINISHED)
			
			d_list = dCards.split(",")
			for i in range(5):
				if i < len(d_list) and d_list[i] and d_list[i] != "0":
					self.dealerCardTexts[i].SetText(self.GetCardName(d_list[i]))
				else:
					self.dealerCardTexts[i].SetText("")
		except:
			import exception
			exception.LogException()

	def OnUpdate(self):
		pass
