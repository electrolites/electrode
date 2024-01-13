"""
Wraps the wx toggle button for electrode.
"""
import wx
from typing import Callable

class ToggleButton(wx.ToggleButton):
	def __init__(self, parent, label: str, onToggel: None | Callable = None, initialState: bool = False):
		super().__init__(parent, label = label)
		if onToggel is not None:
			self.Bind(wx.EVT_TOGGLEBUTTON, onToggel)