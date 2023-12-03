"""
Stores all the pySimpleGuiWx elements for electrode.
"""
import PySimpleGUIWx as sg

class _ElementsMeta:
	def __getattr__(cls, name: str):
		names=[n.__name__ for n in sg.Element.__subclasses__()]
		correspondence=list(zip(names, sg.Element.__subclasses__()))
		if name in names:
			return correspondence[names.index(name)][1]

	def __dir__(cls):
		return [n.__name__ for n in sg.Element.__subclasses__()]

class Elements(metaclass = _ElementsMeta):
	"""Represents the elements class."""