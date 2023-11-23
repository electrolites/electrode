"""
Keyboard input class for electrode.
"""
import wx

class Keyboard:
	def __init__(self, wxWindow):
		self.wxWindow=wxWindow
		self._keys=[]
		self._keyCallbacks={}
		self.__setKeyCodes__()
		self.wxWindow.Bind(wx.EVT_KEY_DOWN, self.__onKeyDown__)
		self.wxWindow.Bind(wx.EVT_KEY_UP, self.__onKeyUp__)

	def __onKeyDown__(self, event):
		keyCode=event.GetKeyCode()
		if keyCode in self._keyCallbacks.keys(): self._keyCallbacks[keyCode]()
		event.Skip()

	def __onKeyUp__(self, event):
		self._keys.remove(event.GetKeyCode())
		event.Skip()

	def keyUp(self, keyCode):
		if keyCode in self._keys: return False
		return True

	def keyDown(self, keyCode):
		if keyCode in self._keys: return True
		return False

	def addKeyCallback(self, keyCode, callback):
		if not callable(callback): raise ValueError(f'The value passed to Keyboard.addKeyCallback must be a function. The value {callback} is not a function.')
		self._keyCallbacks[keyCode]=callback

	def removeKeyCallback(self, keyCode):
		if keyCode in self._keyCallbacks.keys(): self._keyCallbacks.pop(keyCode)
		else: raise RuntimeError(f'The key whith keyCode {keyCode} does not have a callback.')

	def __setKeyCodes__(self):
		wxKeys=[name for name in dir(wx) if name.startswith("WXK_")]
		for key in wxKeys: self.__setattr__(f'K_{key[4:]}',getattr(wx,key))