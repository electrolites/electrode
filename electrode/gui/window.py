"""
Window class for electrode.
"""
import wx
from electrode.gui.elements import input

class Window:
	def __init__(self, title: str, app: wx.App | None = None, orientation: wx.VERTICAL | wx.HORIZONTAL = wx.HORIZONTAL, borderWidth: int = 10):
		self.app = app or wx.App()
		self.title=title
		self.orientation=orientation
		self.borderWidth=borderWidth
		self.frame=wx.Frame(None, title=self.title)
		self.panel=wx.Panel(self.frame, name=self.title)
		self.elements=[]
		self._initUi()

	def _initUi(self):
		self.frame.SetSize(600, 800)
		self.frame.Center()

	def show(self):
		if self.shown: return
		self.frame.Show(True)

	def hide(self):
		if not self.shown: return
		self.frame.Show(False)

	def minimize(self):
		if self.minimized: return
		self.frame.Iconize(True)

	def restore(self):
		if self.minimized: self.frame.Iconize(False)
		if self.Maximized: self.frame.Maximize(False)
		if self.isFullScreen: self.frame.ShowFullScreen(False,style=wx.FULLSCREEN_ALL)
		if not self.shown: self.show()

	def Maximize(self):
		if self.Maximized: return
		self.frame.Maximize(True)

	def fullScreen(self):
		if self.isFullScreen: return
		self.frame.ShowFullScreen(True,style=wx.FULLSCREEN_ALL)

	def addElement(self, element):
		self.elements.append(element)
		self._updateLayout()
		return element


	def addInput(self, message: str, initialText: str = "", multiLine=True, hidden=False, enter = True, tab = False):
		return self.addElement(input.Input(self.panel, message, initialText=initialText, multiLine=multiLine, hidden=hidden, enter=enter, tab=tab))

	def removeElement(self, element):
		if not element in self.elements: return
		self.elements.remove(element)
		self._updateLayout()

	def _updateLayout(self):
		sizer=wx.BoxSizer(self.orientation)
		for element in self.elements:
			sizer.Add(element, proportion=1, flag=wx.EXPAND | wx.ALL, border=self.borderWidth)
		self.panel.SetSizer(sizer)
		self.frame.Layout()

	@property
	def shown(self):
		return self.frame.IsShown()

	@property
	def minimized(self):
		return self.frame.IsIconized()

	@property
	def isFullScreen(self):
		return self.frame.IsFullScreen()

	@property
	def Maximized(self):
		return self.frame.IsMaximized()