"""
Sound managment classes for Electrode.
"""
from itertools import chain
import cyal
from .pool import pool as Pool
from .sound import Sound
from .group import Group, soundFactoryType
from utils import convertToCyalCoordinates

class Manager:
	def __init__(self, path: str, device: cyal.Device | None=None, context: cyal.Context | None=None):
		self.device = device or cyal.Device()
		self.context=context or cyal.Context(self.device, make_current=True, hrtf_soft=1)
		self.alListener=self.context.listener
		self.alListener.orientation = [0, 0, -1, 0, 1, 0]
		self.alListener.position = [0, 0, 0]
		self.pool=Pool(self.context, path)
		self.oneShotSounds: list[Sound]=[]
		self.sounds: list[Sound]=[]

	def newSound(self, filePath: str, OneShot= False, **kwargs):
		s=Sound(self.context,self.pool.get(filePath),**kwargs)
		if OneShot==True:
			if s.looping==True: raise ValueError("Looping must be False if oneShot is true.")
			self.oneShotSounds.append(s)
		else: self.sounds.append(s)
		return s

	def newOneShotSound(self, filePath: str, **kwargs): return self.newSound(filePath, True, **kwargs)

	def newGroup(self, soundFactory: soundFactoryType|None=None, **defaults):
		if soundFactory is None: soundFactory=self.newOneShotSound
		return Group(soundFactory, **defaults)

	def tryCleanOneShots(self):
		for s in self.oneShotSounds:
			if s.isStopped: self.oneShotSounds.remove(s)

	def forceCleanOneShots(self):
		for s in self.oneShotSounds:
			if not s.isStopped: s.stop()
		self.oneShotSounds.clear()

	def tryCleanAll(self):
		self.tryCleanOneShots
		for s in self.sounds:
			if s.isStopped: self.sounds.remove(s)

	def forceCleanAll(self):
		self.forceCleanOneShots()
		for s in self.sounds:
			if not s.isStopped: s.stop()
		self.sounds.clear()

	@property
	def listenerPosition(self) -> list[float]:
		return [self.alListener.position[0], self.alListener.position[2]*-1, self.alListener.position[1]]

	@listenerPosition.setter
	def listenerPosition(self, val: list[float]):
		self.alListener.position=convertToCyalCoordinates(val[0], val[1], val[2])

	@property
	def listenerX(self) -> float: return self.listenerPosition[0]

	@listenerX.setter
	def listenerX(self, val: float):
		pos=self.listenerPosition
		self.listenerPosition=[val, pos[1], pos[2]]

	@property
	def listenerY(self) -> float: return self.listenerPosition[1]

	@listenerY.setter
	def listenerY(self, val: float):
		pos=self.listenerPosition
		self.listenerPosition=[pos[0], val, pos[2]]

	@property
	def listenerZ(self) -> float: return self.listenerPosition[2]

	@listenerZ.setter
	def listenerZ(self, val: float):
		pos=self.listenerPosition
		self.listenerPosition=[pos[0], pos[1], val]

	def push(self):
		# Call on every itoration of the event loop.
		for s in chain(self.oneShotSounds, self.sounds):
			if not s.playedOnce: s.play()
		self.tryCleanOneShots()