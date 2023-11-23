"""
Custom gui element for electrode.
"""
from gui.window import Window

class Element:
			def __init__(self):
		self.layout=[]

	def activate(self, window: Window):
		window.addElements(*self.layout)

	def destroy(self):
		for e in self.layout:
			e.update(visible=False)