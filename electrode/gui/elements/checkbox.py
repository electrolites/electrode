"""
Wraps wx checkbox for electrode.
"""
import wx

class CheckBox(wx.CheckBox):
	def __init__(self, parent, label: str, initialState :int = 0, threeWay: bool = False):
		style=wx.CHK_2STATE
		if threeWay: style=wx.CHK_3STATE
		super().__init__(parent,label=label, style=style)	
		if initialState==1 or initialState>1 and not threeWay: self.SetValue(True)
		elif initialState>1 and threeWay: self.Set3StateValue(wx.CHK_UNDETERMINED)
		else: self.SetValue(False)