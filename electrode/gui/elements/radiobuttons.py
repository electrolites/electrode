"""
Wraps wx radio box for electrode.
"""
from typing import Callable
import wx

class RadioButtons(wx.RadioBox):
	def __init__(self, parent, label: str, choices: list[str], onSelect: Callable | None =None):
		super().__init__(parent, label = label, choices = choices, )
		if onSelect is not None:
			self.Bind(wx.EVT_RADIOBOX, onSelect)

	