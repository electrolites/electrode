"""
Bridges wx event system to electrodes event system.
"""
import asyncio
import wx
from electrode.gui.bridge import wxEvent

class EventBridge:
	def __init__(self, eventManager):
		self.eventManager = eventManager
		self.eventMap = {}
		self.registerWxEvents()

	def registerWxEvents(self):
		wxEvents = [e for e in dir(wx) if e.startswith("EVT_")]
		for e in wxEvents:
			if not  isinstance(getattr(wx, e), wx.PyEventBinder): continue
			asyncio.create_task(self.eventManager.register("gui_"+e[4:].lower(), wxEvent.WxEvent))
			self.eventMap[getattr(wx, e).typeId] = e

	def postEvent(self, event: wx.Event):
		eventObject = event.GetEventObject()
		eventType = self.eventMap[event.GetEventType()]
		asyncio.create_task(self.eventManager.postEvent("gui_"+eventType[4:].lower(), wxObject = eventObject, wxEvent = event))