"""
Window class for electrode.
"""
from typing import Callable
import threading
import wx
import wxasync
from electrode.gui.elements import input, checkbox, button, slider, combobox, spinbutton, listbox, radiobuttons, progressbar, treeview

class Window:
	def __init__(self, title: str, app: wxasync.WxAsyncApp | None = None, orientation: wx.VERTICAL | wx.HORIZONTAL = wx.HORIZONTAL, borderWidth: int = 10):
		self.app = app or wxasync.WxAsyncApp(sleep_duration= 0.002)
		self._title=title
		self.orientation=orientation
		self.borderWidth=borderWidth
		self.elements={}
		self._initUi()

	def _initUi(self):
		self.frame=wx.Frame(None, title=self._title)
		self.panel=wx.Panel(self.frame, name=self.title)
		self.frame.SetSize(600, 800)
		self.frame.Center()

	def show(self):
		if self.shown: return
		self.frame.Show(True)
		children=self.panel.GetChildren()
		if len(children)>0: wx.CallAfter(children[0].SetFocus)

	def hide(self):
		if not self.shown: return
		self.frame.Show(False)

	def minimize(self):
		if self.minimized: return
		self.frame.Iconize(True)

	def restore(self):
		if self.minimized: self.frame.Iconize(False)
		if self.Maximized: self.frame.Maximize(False)
		if self.isFullScreen: self.frame.ShowFullScreen(False,style=wx.FULLSCREEN_ALL)
		if not self.shown: self.show()

	def Maximize(self):
		if self.Maximized: return
		self.frame.Maximize(True)

	def fullScreen(self):
		if self.isFullScreen: return
		self.frame.ShowFullScreen(True,style=wx.FULLSCREEN_ALL)

	def adElement(self, element, *args, **kwargs):
		textLabel = wx.StaticText(self.panel, label = args[1])
		element = element(*args, **kwargs)
		self.elements[textLabel]=element
		self._updateLayout()
		return element

	def adInput(self, message: str, initialText: str = "", multiLine: bool = True, hidden: bool = False, enter: bool = True, tab: bool = False, readOnly: bool = False):
		return self.adElement(input.Input, self.panel, message, initialText=initialText, multiLine=multiLine, hidden=hidden, enter=enter, tab=tab, readOnly =readOnly)

	def adCheckBox(self, label: str, initialState :int = 0, threeWay: bool = False):
		return self.adElement(checkbox.CheckBox, self.panel, label, initialState = initialState, threeWay = threeWay)

	def adButton(self, label: str, callback: Callable | None = None):
		return self.adElement(button.Button, self.panel, label, callback=callback)

	def adSlider(self, label: str, minValue: int = 0, maxValue: int = 100, initialValue: int = 0, onChange: Callable|  None = None, vertical :bool = True):
		return self.adElement(slider.Slider, self.panel, label, minValue=minValue, maxValue=maxValue, initialValue=initialValue, onChange=onChange, vertical = vertical)

	def adComBobox(self, label: str, choices: list[str], initialSelection: int = 0, onSelect: Callable | None = None, readOnly: bool =True):
		return self.adElement(combobox.ComboBox, self.panel, label, choices=choices.copy(), initialSelection = initialSelection, onSelect = onSelect, readOnly = readOnly)

	def adSpinButton(self, label: str, initialValue: int = 0, minValue: int = 0, maxValue: int = 100, aeros: bool = True, wrap: bool = False):
		return self.adElement(spinbutton.SpinButton, self.panel, label, initialValue = initialValue, minValue = minValue, maxValue = maxValue,  aeros = aeros, wrap = wrap)

	def adListBox(self, label: str, choices: list[str], onSelect: Callable | None = None, multiSelect: bool = False):
		self.adElement(listbox.ListBox, self.panel, label, choices, onSelect = onSelect, multiSelect = multiSelect)

	def adRadioButtons(self, label: str, choices: list[str], onSelect: Callable | None =None):
		self.adElement(radiobuttons.RadioButtons, self.panel, label, choices, onSelect = onSelect)

	def adProgressBar(self, label: str, maxValue: int = 100, vertical: bool = True):
		return self.adElement(progressbar.ProgressBar, self.panel, label, maxValue = maxValue, vertical = vertical)

	def adTreeView(self, label: str, onSelect: Callable | None = None, onCollapse: Callable | None = None, onExpande: Callable | None = None, onActivate: Callable | None = None, allowMultiSelect: bool  = False, banishRootNode: bool = True):
		return self.adElement(treeview.TreeView, self.panel, label, onSelect = onSelect, onCollapse = onCollapse, onExpande = onExpande, onActivate = onActivate, allowMultiSelect = allowMultiSelect, banishRootNode = banishRootNode)

	def removeElement(self, element):
		if not element in self.elements.values(): return
		for k,v in self.elements.items():
			if v ==element: self.elements.pop(k)
		self._updateLayout()

	def _updateLayout(self):
		sizer=wx.BoxSizer(self.orientation) if self.panel.GetSizer() is None else self.panel.GetSizer()
		for child in list(self.panel.GetChildren()):
			if child not in self.elements.keys() and child not in self.elements.values():
				self.panel.RemoveChild(child)
				child.Destroy()
		sizer.Clear()
		for labelText, element in self.elements.items():
			elementSizer=wx.BoxSizer(self.orientation)
			existingSizer, textSizer=element.GetContainingSizer(), labelText.GetContainingSizer()
			if textSizer is not None: textSizer.Detach(labelText)
			elementSizer.Add(labelText, proportion=1, flag=wx.ALL, border=self.borderWidth)
			if existingSizer is not None: existingSizer.Detach(element)
			elementSizer.Add(element, proportion=1, flag=wx.EXPAND | wx.ALL, border=self.borderWidth)
			sizer.Add(elementSizer, proportion=1, flag=wx.EXPAND | wx.ALL, border=self.borderWidth)
		self.panel.SetSizer(sizer)
		self.frame.Layout()
		self.frame.Fit()

	@property
	def shown(self):
		return self.frame.IsShown()

	@property
	def minimized(self):
		return self.frame.IsIconized()

	@property
	def isFullScreen(self):
		return self.frame.IsFullScreen()

	@property
	def Maximized(self):
		return self.frame.IsMaximized()

	@property
	def title(self):
		return self._title

	@title.setter
	def title(self, value: str):
		self._title=value
		self.frame.SetTitle(value)