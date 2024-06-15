"""
Wraps wx tree control and wx tree item for electrode.
"""
from typing import Coroutine
import wx
from wxasync import AsyncBind

class TreeView(wx.TreeCtrl):
	def __init__(self, parent, label: str, onSelect: Coroutine | None = None, onCollapse: Coroutine | None = None, onExpande: Coroutine | None = None, onActivate: Coroutine | None = None, allowMultiSelect: bool  = False, banishRootNode: bool = True):
		style = wx.TR_MULTIPLE if allowMultiSelect == True else wx.TR_SINGLE
		if banishRootNode == True:
			style |= wx.TR_HIDE_ROOT
		super().__init__(parent, style = style)
		self.SetLabel(label)
		if onSelect is not None:
			AsyncBind(wx.EVT_TREE_SEL_CHANGED, onSelect, self)
		if onCollapse is not None:
			AsyncBind(wx.EVT_TREE_ITEM_COLLAPSED, onCollapse, self)
		if onExpande is not None:
			AsyncBind(wx.EVT_TREE_ITEM_EXPANDED, onExpande, self)
		if onActivate is not None:
			AsyncBind(wx.EVT_TREE_ITEM_ACTIVATED, onActivate, self)