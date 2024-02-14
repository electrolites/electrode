"""
Entity class for electrode.
"""
from abc import ABC, abstractmethod

class Entity(ABC):
	@abstractmethod
	def __init(self, x: float, y: float, z: float):
		pass

	@abstractmethod
	def move(self, x: float, y: float, z: float):
		pass