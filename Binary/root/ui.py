# Search in class ExpandedImageBox(ImageBox):

		ImageBox.__init__(self, layer)

# Add after

		if app.ENABLE_BLACKJACK_GAME:
			self.onMoveDoneFunc=None
			self.onMoveDoneArgs=None

# Add in class ExpandedImageBox(ImageBox):

	if app.ENABLE_BLACKJACK_GAME:
		def GetRotation(self):
			return wndMgr.GetRotation(self.hWnd)
		def MoveStart(self):
			wndMgr.MoveStart(self.hWnd)
		def MoveStop(self):
			wndMgr.MoveStop(self.hWnd)
		def SetMovePos(self, x, y):
			wndMgr.SetMovePos(self.hWnd, x, y)
		def SetMoveSpeed(self, speed):
			wndMgr.SetMoveSpeed(self.hWnd, speed)
		def SetMoveFunc(self, func, *args):
			self.onMoveDoneFunc = __mem_func__(func)
			self.onMoveDoneArgs = args
		def OnMoveDone(self):
			if self.onMoveDoneFunc:
				apply(self.onMoveDoneFunc, self.onMoveDoneArgs)

