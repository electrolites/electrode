"""
Sound Group class for electrode.
"""
from typing import Callable, Any
from weakref import WeakSet
from .sound import Sound
from .pool import pool as Pool
from electrode.utils import convertToCyalCoordinates

soundFactoryType = Callable[[str, Any], Sound]

class Group:
	def __init__(self, soundFactory: soundFactoryType, **defaults):
		self.soundFactory=soundFactory
		self.defaults=defaults
		self._position=[0, 0, 0]
		self.__destroyed__=False
		self.sounds=WeakSet[Sound]()

	def destroy(self):
		if self.__destroyed__: return
		self.__destroyed__=True
		for sound in self.sounds:
			if sound.isPlaying: sound.stop()
		self.sounds.clear()

	def addSound(self, sound: Sound):
		self.sounds.add(sound)
		if not sound.direct: sound.position=convertToCyalCoordinates(self.position)

	def newSound(self, filePath: str, **kwargs):
		sound=self.soundFactory(filePath, **{**self.defaults, **kwargs})
		self.addSound(sound)
		return sound

	@property
	def position(self):
		return self._position

	@position.setter
	def position(self, val: list):
		self._position=val
		for sound in self.sounds:
			if not sound.direct: sound=convertToCyalCoordinates(*val)

	@property
	def x(self):
		return self.position[0]

	@x.setter
	def x(self, val: float):
		pos=self.position
		self.position=[val, pos[1], pos[2]]

	@property
	def y(self):
		return self.position[1]

	@y.setter
	def y(self, val: float):
		pos=self.position.copy
		self.position=[pos[0], val, pos[2]]

	@property
	def z(self):
		return self.position[2]

	@z.setter
	def z(self, val: float):
		pos=self.position
		self.position=[pos[0], pos[1], val]

	def __del__(self):
		if not self.__destroyed__: self.destroy()

	@property
	def destroyed(self):
		return self.__destroyed__