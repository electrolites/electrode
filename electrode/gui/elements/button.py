"""
Wraps wx button for electrode.
"""
from types import coroutine
import wx
from wxasync import AsyncBind
from typing import Callable, Coroutine

class Button(wx.Button):
	def __init__(self, parent, label: str, callback: Coroutine | None = None):
		super().__init__(parent,label=label)
		if callback is not None: AsyncBind(wx.EVT_BUTTON, callback, self)
