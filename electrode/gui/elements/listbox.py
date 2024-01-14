"""

Wraps wx list box for electrode.
"""
import wx
from typing import Callable

class ListBox(wx.ListBox):
	def __init__(self, parent, label: str, choices: list[str], onSelect: Callable | None = None, multiSelect: bool = False):
		style = wx.LB_MULTIPLE if multiSelect else wx.LB_SINGLE
		style |= wx.LB_HSCROLL
		style |= wx.LB_NEEDED_SB
		super().__init__(parent, choices = choices, style = style)
		self.SetLabel(label)
		if onSelect is not None:
			self.Bind(wx.EVT_LISTBOX, onSelect)

	def removeItem(self, item: str):
		index = self.FindString(item)
		if index != wx.NOT_FOUND: self.Delete(index)

	def selectItem(self, item: str):
		index = self.FindString(item)
		if index != wx.NOT_FOUND: self.SetSelection(index)

	def deselectAll(self):
		self.SetSelection(wx.NOT_FOUND)

	