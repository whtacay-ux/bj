import ui
import net
import chat
import player
import app
import localeInfo

class BlackjackWindow(ui.ScriptWindow):
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
			
			self.hitBtn = self.GetChild("HitButton")
			self.standBtn = self.GetChild("StandButton")
			self.splitBtn = self.GetChild("SplitButton")
			self.doubleBtn = self.GetChild("DoubleButton")
			self.insuranceBtn = self.GetChild("InsuranceButton")
			self.surrenderBtn = self.GetChild("SurrenderButton")

			self.playerScore = self.GetChild("PlayerScoreValue")
			self.dealerScore = self.GetChild("DealerScoreValue")

			# Slot positions for cards
			self.playerSlots = []
			for i in range(5):
				self.playerSlots.append(self.GetChild("PlayerCardSlot_%d" % i))
				
			self.dealerSlots = []
			for i in range(5):
				self.dealerSlots.append(self.GetChild("DealerCardSlot_%d" % i))

			self.titleBar.SetCloseEvent(ui.__mem_func__(self.Close))
			self.betBtn.SetEvent(ui.__mem_func__(self.__OnBet))
			self.hitBtn.SetEvent(ui.__mem_func__(self.__OnHit))
			self.standBtn.SetEvent(ui.__mem_func__(self.__OnStand))
			self.splitBtn.SetEvent(ui.__mem_func__(self.__OnSplit))
			self.doubleBtn.SetEvent(ui.__mem_func__(self.__OnDouble))
			self.insuranceBtn.SetEvent(ui.__mem_func__(self.__OnInsurance))
			self.surrenderBtn.SetEvent(ui.__mem_func__(self.__OnSurrender))
			
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

	def __OnBet(self):
		amount = self.betInput.GetText()
		if not amount.isdigit():
			return
		net.SendChatPacket("/blackjack bet " + amount)

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

	def UpdateGame(self, data):
		# data is a string like "1000 21 17" (bet pScore dScore)
		try:
			tokens = data.split()
			if len(tokens) >= 3:
				self.playerScore.SetText(tokens[1])
				self.dealerScore.SetText(tokens[2])
				# Here we could disable/enable buttons based on state
		except:
			pass

	def OnUpdate(self):
		pass
