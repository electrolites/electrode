"""
Wx event protocol for electrode.
"""
from typing import Any, Protocol, runtime_checkable
from wx import Event as wxPythonEvent

@runtime_checkable
class WxEvent(Protocol):
	wxObject: Any
	wxEvent: wxPythonEvent