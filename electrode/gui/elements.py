"""
Stores all the pySimpleGuiWx elements for electrode.
"""
import PySimpleGUIWx as sg

class _ElementsMeta:
	def __getattr__(cls, name: str):
		names=[n.__name__ for n in sg.Element.__subclasses__()]
		correspondence=zip(names,sg.Element.__subclasses__())
		if name in names:
			return 