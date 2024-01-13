"""
Wraps wx spin control for electrode
"""
import wx

class SpinButton(wx.SpinCtrl):
	def __init__(self, parent, label: str, initialValue: int = 0, minValue: int = 0, maxValue: int = 100, aeros: bool = True, wrap: bool = False):
		if minValue>maxValue: raise ValueError(f'The minimum value of a spin button can not be grater than its maximum value. {minValue} is grater than {maxValue}.')
		elif maxValue<minValue: raise ValueError(f'The maximum value of a spin button can not be less than its minimum value. {maxValue} is less than {minValue}.')
		if initialValue<minValue: initialValue=minValue
		elif initialValue>maxValue: initialValue=maxValue
		style = wx.ALIGN_LEFT
		if aeros == True: style |= wx.SP_ARROW_KEYS
		if wrap == True: style |= wx.SP_WRAP
		super().__init__(parent, value = str(initialValue), min = minValue, max = maxValue, style = style)
		self.SetLabel(label)