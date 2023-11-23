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
		self.customElements=[]

	def start(self):
		self.window=sg.Window(self.title, [self.column])

	def stop(self):
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


	def addElement(self, element):
		newLayout=self.layout.copy()
		newLayout.append(element)
		self.layout=newLayout

	def addElements(self, *args):
		newLayout=self.layout.copy()
		newLayout.extend(*args)
		self.layout=newLayout

	def removeElement(self, key):
		self.window[key].update(visible=False)

	def addCustomElement(self, element):
		self.customElements.append(element)
		element.activate(self)

	def findElement(self, key):
		return self.window.find_element(key)

	def push(self):
		return self.window.read()