"""
Wrapps wx comboBox for electrode.
"""
import wx
from typing import Callable

class ComboBox(wx.ComboBox):
	def __init__(self, parent, label: str, choices: list[str], initialSelection: int = 0, onSelect: Callable | None = None, readOnly: bool = True):
		choiceList=choices.copy()
		style=wx.CB_READONLY if readOnly else wx.CB_DROPDOWN
		super().__init__(parent, choices=choiceList, style = style)
		if onSelect is not None:
			self.Bind(wx.EVT_COMBOBOX, onSelect)
		self.SetLabel(label)
		self.SetSelection(initialSelection)