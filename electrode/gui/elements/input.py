"""
Wraps wx textctrl for electrode.
"""
import wx

class Input(wx.TextCtrl):
	def __init__(self, parent, message: str, initialText: str = "", multiLine: bool = True, hidden: bool = False, enter: bool = True, tab :bool = False, readOnly: bool = False):
		style=wx.TE_LEFT
		if multiLine==True: style = wx.TE_MULTILINE
		if hidden==True: style |= wx.TE_PASSWORD
		if readOnly == True: style = wx.TE_READONLY
		if enter==True: style |= wx.TE_PROCESS_ENTER
		if tab==True: style |= wx.TE_PROCESS_TAB
		super().__init__(parent, value=initialText, style = style)
		self.SetLabel(message)