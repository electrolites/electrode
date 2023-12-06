"""
Surface classes for electrode.
"""
from coordinateContainer import CoordinateContainer
from timer import Timer

class Surface(CoordinateContainer):
	def __init__(self, minX: int, maxX: int, minY: int, maxY: int, minZ: int, maxZ: int, tile: str):
		super().__init__(minX, maxX, minY, maxY, minZ, maxZ)
		self.tile=tile

class VanishingSurface(surface):
	def __init__(self, minX: int, maxX: int, minY: int, maxY: int, minZ: int, maxZ: int, tile: str,sound: str, onTime: int, offTime=0):
		super().__init__(minX, maxX, minY, maxY, minZ, maxZ,tile)
		self.sound=sound
		self.onTime=onTime
		if offTime==0: self.offTime=onTime
		else: self.offTime=offTime
		self._active=True
		self.timer=timer.Timer()

	@property
	def active(self):
		if self._active==True and self.timer.time>=self.onTime:
			self._active=False
			self.timer.restart()
		elif self._active==False and self.timer.time>=self.offTime:
			self._active=True
			self.timer.restart()
		return self._active

	@active.setter
	def active(self,act: bool):
		self._active=act
		self.timer.restart()