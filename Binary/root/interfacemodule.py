# Add

if app.ENABLE_BLACKJACK_GAME:
	import uiBlackJack

# Search

		self.windowOpenPosition = 0

# Add after

		if app.ENABLE_BLACKJACK_GAME:
			self.wndBlackJackGame = None

# Search

	def Close(self):

#Add after

		if app.ENABLE_BLACKJACK_GAME:
			if self.wndBlackJackGame:
				self.wndBlackJackGame.Close()
				self.wndBlackJackGame.Destroy()
				self.wndBlackJackGame=None

# add

	if app.ENABLE_BLACKJACK_GAME:
		def MakeBlackJackGameWindow(self):
			if self.wndBlackJackGame == None:
				self.wndBlackJackGame = uiBlackJack.BlackJackGame()
		def OpenBlackJackGame(self):
			self.MakeBlackJackGameWindow()
			if self.wndBlackJackGame.IsShow():
				self.wndBlackJackGame.Close()
			else:
				self.wndBlackJackGame.Open()
		def BJAddNewCard(self, isBot, cardType, cardIndex, returnValue):
			self.MakeBlackJackGameWindow()
			self.wndBlackJackGame.AddNewCard(int(isBot), int(cardType), int(cardIndex), int(returnValue))
		def BJSetGameMode(self, gameKey):
			self.MakeBlackJackGameWindow()
			self.wndBlackJackGame.SetGameMode(int(gameKey))
		def BJShowGameStatus(self, isBotWin):
			self.MakeBlackJackGameWindow()
			self.wndBlackJackGame.ShowGameStatus(int(isBotWin))
