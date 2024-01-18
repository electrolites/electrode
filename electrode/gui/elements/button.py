"""
Wraps wx button for electrode.
"""
import wx
from typing import Callable

class Button(wx.Button):
	def __init__(self, parent, label: str, callback: Callable | None = None):
		super().__init__(parent,label=label)
		if callback is not None: self.Bind(wx.EVT_BUTTON, callback)