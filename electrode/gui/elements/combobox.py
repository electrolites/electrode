"""
Wrapps wx comboBox for electrode.
"""
import wx
from wxasync import AsyncBind
from typing import Callable, Coroutine

class ComboBox(wx.ComboBox):
	def __init__(self, parent, label: str, choices: list[str], initialSelection: int = 0, onSelect: Coroutine | None = None, readOnly: bool = True):
		choiceList=choices.copy()
		style=wx.CB_READONLY if readOnly else wx.CB_DROPDOWN
		super().__init__(parent, choices=choiceList, style = style)
		if onSelect is not None:
			AsyncBind(wx.EVT_COMBOBOX, onSelect, self)
		self.SetLabel(label)
		self.SetSelection(initialSelection)
