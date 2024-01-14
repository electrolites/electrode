"""
Wraps wx slider for electrode.
"""
import wx
from typing import Callable

class Slider(wx.Slider):
	def __init__(self, parent, label: str, minValue: int = 0, maxValue: int = 100, initialValue: int = 0, onChange: Callable | None  = None, vertical: bool = True):
		if minValue>maxValue: raise ValueError(f'The minimum value of a slider can not be grater than its maximum value. {minValue} is grater than {maxValue}.')
		elif maxValue<minValue: raise ValueError(f'The maximum value of a slider can not be less than its minimum value. {maxValue} is less than {minValue}.')
		if initialValue<minValue: initialValue=minValue
		elif initialValue>maxValue: initialValue=maxValue
		style=wx.SL_VERTICAL if vertical == True else wx.SL_HORIZONTAL
		super().__init__(parent, value=initialValue, minValue=minValue, maxValue=maxValue, style = style)
		self.SetLabel(label)
		if onChange is not None:
			self.Bind(wx.EVT_SLIDER, onChange)
		self.Bind(wx.EVT_KEY_DOWN, self._onKey)

	def _onKey(self, wxEvent: wx.Event):
		code = wxEvent.GetKeyCode()
		value=self.GetValue()
		match code:
			case wx.WXK_DOWN: value-=1
			case wx.WXK_UP: value+=1
			case wx.WXK_PAGEDOWN: value-=10
			case wx.WXK_PAGEUP: value+=10
			case wx.WXK_HOME: value = self.GetMax()
			case wx.WXK_END: value = self.GetMin()
			case _:
				wxEvent.Skip()
				return
		self.SetValue(value)
		event = wx.CommandEvent(wx.EVT_SLIDER.typeId, self.GetId())
		event.SetEventObject(self)
		self.ProcessEvent(event)