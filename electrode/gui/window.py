"""
Window class for electrode.
"""
import PySimpleGUIWx as sg
	
class window:
	def __init__(self, title: str, layOut: list=[]):
		self.title=title
		self._layout=layOut
		self.active=False
		self.column=sg.Column(self.layout)
		

	def launch(self):
		self.window=sg.Window(self.title, [self.column])

	def close(self):
		self.window.close()

	@property
	def layout(self):
		return self._layout

	@layout.setter
	def layout(self, val: list):
		self._layout=val
		self.column.update(visible=False)
		self.column=sg.Column(val)
		self.window.add_row(self.column)

	def addElement(self, element: sg.Element):
		newLayout=self.layout.copy()
		newLayout.append(element)
		self.layout=newLayout
		self.column.Update()

	def addElements(self, *args):
		newLayout=self.layout.copy()
		newLayout.extend(*args)
		self.layout=newLayout

	def removeElement(self, key):
		self.window[key].update(visible=False)

	def findElement(self, key):
		return self.window.find_element(key)

	def push(self):
		return self.window.read()

	def __getattr_(self, name: str) -> Any:
		if hasattr(self, name): return self.__dict__[name]
		else: return getattr(self.window,name)