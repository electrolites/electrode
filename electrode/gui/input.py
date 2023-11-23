"""
Input gui element for electrode.
"""
import PySimpleGUIWx as sg
from gui.element import Element

class Input(Element):
	def __init__(self, DefaultText: str="", multiLine: bool=True, charCallback=None, dellCallback=None, enterCallback=None, **kwargs):
		self.text=DefaultText
		self.charCallback=charCallback
		self.dellCallback=dellCallback
		self.enterCallback=enterCallback
		self.element=sg.Multiline(default_text=self.text, enable_events=True, **kwargs) if multiLine==True else sg.Input(default_text=self.text, enable_events=True, **kwargs)
		self.layout=[self.element]
		self.window=None

	def push(self):
		oldText=self.text
		self.text=self.element.get()
		if len(oldText)>self.text and self.charCallback is not None:
			char=self.text[len(oldText)+1]
			if callable(self.charCallback): self.charCallback(char)
			else: raise RuntimeError(f'The charCallback {self.charCallback} of the input element class {self}. is not callable.')
		elif len(oldText)<self.text and self.dellCallback is not None:
			char=oldText[len(self.text)]
			if callable(self.dellCallback): self.dellCallback(char)
			else: raise RuntimeError(f'The dellCallback {self.dellCallback} of the input element class {self}. is not callable.')



	def activate(self, window):
		super().activate(window)
		self.window=window