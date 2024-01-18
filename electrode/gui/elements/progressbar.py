"""
Wraps wx gage for electrode.
"""
from typing import Callable
import wx

class ProgressBar(wx.Gauge):
	def __init__(self, parent, label: str, maxValue: int = 100, vertical: bool = True):
		style = wx.GA_VERTICAL if vertical else wx.GA_HORIZONTAL
		super().__init__(parent, range = maxValue, style = style)
		self.SetLabel(label)