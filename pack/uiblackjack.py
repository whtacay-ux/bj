import ui
import net
import chat
import player
import app
import localeInfo

class Card(ui.ExpandedImageBox):
	def __init__(self, parent, cardId, isDealer=False):
		ui.ExpandedImageBox.__init__(self)
		self.SetParent(parent)
		self.cardId = int(cardId)
		self.isDealer = isDealer
		
		# User's logic: (cid - 1) / 13 = suit, (cid - 1) % 13 = rank
		if self.cardId == 0: # Secret card
			self.LoadImage("d:/ymir work/ui/game/black_jack/secret_card.tga")
		else:
			suit = (self.cardId - 1) / 13
			rank = (self.cardId - 1) % 13 + 1 # 1-13
			self.LoadImage("d:/ymir work/ui/game/black_jack/%d.tga" % rank)
			
			self.suitImg = ui.ImageBox()
			self.suitImg.SetParent(self)
			self.suitImg.LoadImage("d:/ymir work/ui/game/black_jack/small_type/%d.tga" % suit)
			self.suitImg.SetPosition(5, 5)
			self.suitImg.Show()
			
		self.Show()

	def __del__(self):
		ui.ExpandedImageBox.__del__(self)

class BlackjackWindow(ui.ScriptWindow):
	STATE_WAITING_BET = 0
	STATE_PLAYING = 1
	STATE_FINISHED = 2

	CARD_SUITS = ["Maça", "Kupa", "Karo", "Sinek"]
	CARD_RANKS = ["As", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Vale", "Kız", "Papaz"]

	def __init__(self):
		ui.ScriptWindow.__init__(self)
		self.isLoaded = False
		self.playerCards = []
		self.dealerCards = []
		self.resultImage = None

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
			
			self.resultImage = ui.ImageBox()
			self.resultImage.SetParent(self.board)
			self.resultImage.SetPosition(210 - 100, 150) # Center-ish
			self.resultImage.Hide()
			
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
		self.playerCards = []
		self.dealerCards = []
		if self.resultImage: self.resultImage.Hide()
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
			
			if self.resultImage: self.resultImage.Hide()
			
			nState = int(state)
			self.__SetButtonState(nState)
			
			# Update cards
			p_list = [int(x) for x in pCards.split(",") if x and x != ""]
			d_list = [int(x) for x in dCards.split(",") if x and x != ""]
			
			# Dealer secret card logic if playing
			if nState == self.STATE_PLAYING and len(d_list) > 0:
				if len(d_list) == 1:
					d_list.append(0) # Secret card
			
			# Clear old cards if count mismatch or reset needed
			if len(p_list) < len(self.playerCards) or len(d_list) < len(self.dealerCards):
				self.playerCards = []
				self.dealerCards = []

			# Refill Player Cards
			for i in range(len(p_list)):
				if i >= len(self.playerCards):
					card = Card(self.board, p_list[i])
					# Animate from deck location (top right-ish)
					card.SetPosition(350, 50)
					card.SetMovePos(50 + (i * 35), 180)
					card.SetMoveSpeed(15)
					card.MoveStart()
					self.playerCards.append(card)
				else:
					if self.playerCards[i].cardId != p_list[i]:
						# Replace if ID changed (shouldn't happen often in BJ unless reset)
						self.playerCards[i].Hide()
						self.playerCards[i] = Card(self.board, p_list[i])
						self.playerCards[i].SetPosition(50 + (i * 35), 180)

			# Refill Dealer Cards
			for i in range(len(d_list)):
				if i >= len(self.dealerCards):
					card = Card(self.board, d_list[i], True)
					card.SetPosition(350, 50)
					card.SetMovePos(50 + (i * 35), 90)
					card.SetMoveSpeed(15)
					card.MoveStart()
					self.dealerCards.append(card)
				else:
					if self.dealerCards[i].cardId != d_list[i]:
						self.dealerCards[i].Hide()
						self.dealerCards[i] = Card(self.board, d_list[i], True)
						self.dealerCards[i].SetPosition(50 + (i * 35), 90)

		except:
			import exception
			exception.LogException()

	def ShowResult(self, result, pScore, dScore, dCards):
		try:
			self.playerScore.SetText(str(pScore))
			self.dealerScore.SetText(str(dScore))
			self.__SetButtonState(self.STATE_FINISHED)
			
			# Update dealer cards (flip secret card)
			d_list = [int(x) for x in dCards.split(",") if x and x != ""]
			self.dealerCards = [] # Clear and redraw for result
			for i in range(len(d_list)):
				card = Card(self.board, d_list[i], True)
				card.SetPosition(50 + (i * 35), 90)
				self.dealerCards.append(card)
				
			# Show visual result
			if self.resultImage:
				if "win" in result.lower() or "won" in result.lower() or "tebrikler" in result.lower():
					self.resultImage.LoadImage("d:/ymir work/ui/game/black_jack/won.tga")
				else:
					self.resultImage.LoadImage("d:/ymir work/ui/game/black_jack/lose.tga")
				self.resultImage.Show()

		except:
			import exception
			exception.LogException()

	def OnUpdate(self):
		pass
