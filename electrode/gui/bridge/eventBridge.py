"""
Bridges wx event system to electrodes event system.
"""
from wx import Event as wxPythonEvent
from electrode.gui.bridge import wxEvent

class EventBridge:
	def __init__(self, eventManager):
		self.eventManager = eventManager
		self.registerWxEvents()

	def registerWxEvents(self):
		wxEvents = [e for e in dir(wx) if e.startswith("EVT_")]
		for e in wxEvents:
			self.eventManager.register("gui_"+e[4:].lower(), wxEvent)

	async def postEvent(self, event: wxPythonEvent):
		eventObject = event.GetEventObject()
		eventType = event.GetEventType()
		await self.eventManager.post("gui_"+eventType[4:], object = eventObject, wxEvent = event)