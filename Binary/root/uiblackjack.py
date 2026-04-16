import ui, app, item, dbg, localeInfo, _weakref, net

IMG_DIR = "black_jack/"

#Config
betList = [ [100, 50011], [200, 30623], [300, 33028], [400, 33030]]

def GetCardIndexToValue(cardsList):
	value = 0
	aceList = []
	for card in cardsList:
		if card[1] >= 11 and card[1] <= 13:
			value+=10
			continue
		elif card[1] == 1:
			aceList.append(card[1])
			continue
		value+=card[1]
	for j in xrange(len(aceList)):
		value+= 11 if j == 0 else 1
	return value

class BlackJackGame(ui.ScriptWindow):
	def __del__(self):
		ui.ScriptWindow.__del__(self)
	def Destroy(self):
		self.ClearDictionary()
		self.__gameData={}
	def Open(self):
		self.Show()
	def Close(self):
		self.Hide()
	def OnPressEscapeKey(self):
		self.Close()
		return True
	def GetGameData(self):
		return self.__gameData
	def __init__(self):
		ui.ScriptWindow.__init__(self)
		self.Destroy()
		self.__LoadWindow()

	def __LoadWindow(self):
		try:
			pyScrLoader = ui.PythonScriptLoader()
			pyScrLoader.LoadScriptFile(self, "UIScript/blackjack_game.py")
			GetObject = self.GetChild
			GetObject("decreaseDealBtn").SAFE_SetEvent(self.__ClickSetBet, True)
			GetObject("increaseDealBtn").SAFE_SetEvent(self.__ClickSetBet, False)
			GetObject("startBtn").SetEvent(self.__ClickStartGame)
			GetObject("standBtn").SetEvent(self.__ClickStand)
			GetObject("newCardBtn").SetEvent(self.__ClickNewCard)
		except:
			import exception
			exception.Abort("BlackJackGame.Initialize")

		self.GetChild("Window").SetCloseEvent(self.Close)
		self.SetCenterPosition()
		self.SetDefaultConfig()
		self.__SetBetType(0)

	def SetGameMode(self, gameKey = -1):
		self.__gameData["gameKey"] = gameKey
		GetObject = self.GetChild
		if gameKey == -1:
			GetObject("standBtn").Hide()
			GetObject("newCardBtn").Hide()
			GetObject("startBtn").Show()
		else:
			GetObject("standBtn").Show()
			GetObject("newCardBtn").Show()
			GetObject("startBtn").Hide()

	def __ClickSetBet(self, isDecrease):
		self.__SetBetType(self.__gameData["betType"]+1 if not isDecrease else self.__gameData["betType"]-1)
	def __SetBetType(self, betIndex):
		global betList
		if betIndex < 0 or betIndex >= len(betList):
			return
		self.__gameData["betType"] = betIndex
		self.GetChild("deal").SetText(str(betList[betIndex][0]))
		item.SelectItem(betList[betIndex][1])
		self.GetChild("reward_item").LoadImage(item.GetIconImageFileName())

	def SetDefaultConfig(self):
		self.SetGameMode(-1)
		self.GetChild("dealer_text").SetText(localeInfo.BLACKJACK_DEALER)
		self.GetChild("me_text").SetText(localeInfo.BLACKJACK_ME)
		self.__gameData["cards"] = []
		self.__gameData["bot_cards"] = []
		self.__gameData["ch_cards"] = []

		self.CheckGameStatus()

	def CheckGameStatus(self):
		statusImage = self.ElementDictionary["statusImage"] if self.ElementDictionary.has_key("statusImage") else None
		if statusImage:
			statusImage.Hide()
			self.ElementDictionary["statusImage"] = None

	def ShowGameStatus(self, isBotWinner):
		self.CheckGameStatus()

		statusImage = ui.ExpandedImageBox()
		statusImage.SetParent(self.GetChild("board"))
		statusImage.SetWindowHorizontalAlignCenter()
		statusImage.SetWindowVerticalAlignCenter()
		statusImage.LoadImage(IMG_DIR+("lose.tga" if isBotWinner else "won.tga"))
		statusImage.SetPosition(statusImage.GetLocalPosition()[0], -(statusImage.GetHeight()/2))
		statusImage.SetAlpha(0.1)
		statusImage.Show()
		self.__gameData["statusAlpha"] = 0.02
		self.__gameData["statusAlphaNextTime"] = app.GetTime() + 0.01
		self.ElementDictionary["statusImage"] = statusImage

		net.SendChatPacket("/blackjack end")

	def OnUpdate(self):
		statusImage = self.ElementDictionary["statusImage"] if self.ElementDictionary.has_key("statusImage") else None
		if statusImage:
			if app.GetTime() > self.__gameData["statusAlphaNextTime"]:
				if self.__gameData["statusAlpha"] >= 1.0:
					return
				self.__gameData["statusAlpha"] += 0.02
				statusImage.SetAlpha(self.__gameData["statusAlpha"])
				self.__gameData["statusAlphaNextTime"] = app.GetTime() + 0.01


	def __ClickStartGame(self):
		self.SetDefaultConfig()

		gameKey = self.__gameData["gameKey"] if self.__gameData.has_key("gameKey") else -1
		if gameKey == -1:
			net.SendChatPacket("/blackjack start {}".format(self.__gameData["betType"]))

	def __ClickStand(self):
		gameKey = self.__gameData["gameKey"] if self.__gameData.has_key("gameKey") else -1
		if gameKey != -1:
			net.SendChatPacket("/blackjack stand {}".format(gameKey))

	def __ClickNewCard(self):
		gameKey = self.__gameData["gameKey"] if self.__gameData.has_key("gameKey") else -1
		if gameKey != -1:
			net.SendChatPacket("/blackjack newcard {}".format(gameKey))

	def OnMoveDone(self):
		self.__ClickStartGame()
		
	def AddNewCard(self, isForBot, cartType, cartIndex, addType = -1, addIndex = -1):
		botCards = self.__gameData["bot_cards"] if self.__gameData.has_key("bot_cards") else []
		playerCards = self.__gameData["ch_cards"] if self.__gameData.has_key("ch_cards") else []

		newCard = Card(cartType, cartIndex)
		newCard.SetParent(self.GetChild("board"))
		newCard.SetPosition(294, 19)
		newCard.SetMovePos(148+(len(botCards if isForBot else playerCards)*19), 47 if isForBot else 120)
		newCard.SetMoveSpeed(10.0)
		newCard.MoveStart()

		self.__gameData["cards"].append(newCard)

		self.__gameData["bot_cards" if isForBot else "ch_cards"].append([cartType, cartIndex])
		self.GetChild("dealer_text" if isForBot else "me_text").SetText((localeInfo.BLACKJACK_DEALER if isForBot else localeInfo.BLACKJACK_ME)+": "+str(GetCardIndexToValue(self.__gameData["bot_cards" if isForBot else "ch_cards"])))

		if addType != -1:
			newCard.SetMoveFunc(self.SetMoveDone, _weakref.proxy(newCard), addType, addIndex)

	def SetMoveDone(self, newCard, addType, addIndex):
		if addType == 99:#done
			self.ShowGameStatus(True if addIndex == 1 else False)
		elif addType == 98:#stand
			gameKey = self.__gameData["gameKey"] if self.__gameData.has_key("gameKey") else -1
			if gameKey != -1:
				net.SendChatPacket("/blackjack stand {}".format(gameKey))
		elif addType == 97:#want_card
			gameKey = self.__gameData["gameKey"] if self.__gameData.has_key("gameKey") else -1
			if gameKey != -1:
				net.SendChatPacket("/blackjack check {}".format(gameKey))

class Card(ui.ExpandedImageBox):
	def __del__(self):
		ui.ExpandedImageBox.__del__(self)
	def Destroy(self):
		self.cardType = cardType
		self.cardIndex = cardIndex
		self.bigTypeImg = None
		self.numberImg = None
		self.smallTypeImg = None
	def __init__(self, cardType, cardIndex):
		ui.ExpandedImageBox.__init__(self)
		self.cardType = cardType
		self.cardIndex = cardIndex
		self.__LoadCard()
	def MakeImage(self, x, y, img):
		image = ui.ExpandedImageBox()
		image.SetParent(self)
		image.AddFlag("not_pick")
		image.LoadImage(img)
		image.SetPosition(x,y)
		image.Show()
		return image
	def __LoadCard(self):
		self.LoadImage(IMG_DIR+"card.tga")
		self.SetScale(49.0 * (1.0/float(self.GetWidth())), 66.0 * (1.0/float(self.GetHeight())))
		self.numberImg = self.MakeImage(7,7,IMG_DIR+("number/{}.tga".format(self.cardIndex)))
		self.numberImg.SetDiffuseColor(1.0 if self.cardType == 1 or self.cardType == 2 else 0.0, 0.0, 0.0, 0.7)
		self.smallTypeImg = self.MakeImage(7,7+self.numberImg.GetHeight()+3,IMG_DIR+("small_type/{}.tga".format(self.cardType)))
		self.smallTypeImg.SetDiffuseColor(1.0, 1.0, 1.0, 0.8)
		img_names = ["j","q","k"]
		bigImage = "big_type/{}.tga".format(img_names[self.cardIndex-11]) if self.cardIndex > 10 else  "big_type/{}.tga".format(self.cardType)
		bigTypeImg = self.MakeImage(8,13,IMG_DIR+bigImage)
		bigTypeImg.SetWindowHorizontalAlignCenter()
		bigTypeImg.SetWindowVerticalAlignCenter()
		bigTypeImg.SetDiffuseColor(1.0, 1.0, 1.0, 0.8)
		self.bigTypeImg = bigTypeImg
		self.Show()
