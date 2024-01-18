"""
Wraps wx tree control and wx tree item for electrode.
"""
from typing import Callable
import wx

class TreeView(wx.TreeCtrl):
	def __init__(self, parent, label: str, onSelect: Callable | None = None, onCollapse: Callable | None = None, onExpande: Callable | None = None, onActivate: Callable | None = None, allowMultiSelect: bool  = False, banishRootNode: bool = True):
		style = wx.TR_MULTIPLE if allowMultiSelect == True else wx.TR_SINGLE
		if banishRootNode == True:
			style |= wx.TR_HIDE_ROOT
		super().__init__(parent, style = style)
		self.SetLabel(label)
		if onSelect is not None:
			self.Bind(wx.EVT_TREE_SEL_CHANGED, onSelect)
		if onCollapse is not None:
			self.Bind(wx.EVT_TREE_ITEM_COLLAPSED, onCollapse)
		if onExpande is not None:
			self.Bind(wx.EVT_TREE_ITEM_EXPANDED, onExpande)
		if onActivate is not None:
			self.Bind(wx.EVT_TREE_ITEM_ACTIVATED, onActivate)