"""
Wx event protocol for electrode.
"""
from typing import Any, Protocol
from wx import Event as wxPythonEvent

class WxEvent(Protocol):
	"""
	Protocol class for registering wx events with electrodes event system.
	"""
	wxEvent: wxPythonEvent
	object: Any
