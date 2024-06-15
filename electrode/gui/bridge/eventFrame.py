"""
Event frame for electrode.
"""
import asyncio
from wx import Frame
import wxasync
from electrode.gui.bridge import eventBridge

class EventFrame(Frame):
	def __init__(self, eventManager, *args, **kw):
		self.eventManager = eventManager
		self.eventBridge = eventBridge.EventBridge(self.eventManager)
		super().__init__(*args, **kw)

	def ProcessEvent(self, event):
		self.eventBridge.postEvent(event)
		return super().ProcessEvent(event)