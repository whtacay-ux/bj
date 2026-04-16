# Search

		self.serverCommander=stringCommander.Analyzer()

# Add before

		if app.ENABLE_BLACKJACK_GAME:
			serverCommandList.update({"BJAddNewCard" : self.interface.BJAddNewCard})
			serverCommandList.update({"BJSetGameMode" : self.interface.BJSetGameMode})
			serverCommandList.update({"BJShowGameStatus" : self.interface.BJShowGameStatus})
			serverCommandList.update({"BJOpenGame" : self.interface.OpenBlackJackGame})

