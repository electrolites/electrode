"""
Wraps wx textctrl for electrode.
"""
import wx

class Input(wx.TextCtrl):
	def __init__(self, parent, message: str, initialText: str = "", multiLine=True, hidden=False, enter = True, tab = False):
		style=wx.TE_LEFT
		if multiLine==True: style = wx.TE_MULTILINE
		if hidden==True: style = wx.TE_PASSWORD
		if enter==True: style |= wx.TE_PROCESS_ENTER
		if tab==True: style |= wx.TE_PROCESS_TAB
		super().__init__(parent, value=initialText, style = style)
		self.SetLabel(message)