"""
Sound class for electrode.
"""
import cyal

class Sound:
	def __init__(self, eventManager, context: cyal.Context, buffer: cyal.Buffer, **kwargs):
		self.context=context
		self.buffer=buffer
		self.alSource=context.gen_source()
		self.alSource.buffer=self.buffer
		self.alSource.spatialize = True
		self.alSource.position=[0.0, 0.0, 0.0]
		self._direct = False
		self.playedOnce=False
		self.eventManager = eventManager
		for key, value in kwargs.items():
			setattr(self, key, value)

	@property
	def x(self):
		return self.position[0]

	async def setX(self, val: float):
		pos=self.position
		await self.setPosition(val, pos[1], pos[2])

	@property
	def y(self):
		return self.position[1]

	async def setY(self, val: float):
		pos=self.position
		await self.setPosition(pos[0], val, pos[2])

	@property
	def z(self):
		return self.position[2]


	async def setZ(self, val: float):
		pos=self.position
		await self.setPosition(pos[0], pos[1], val)

	@property
	def position(self):
		return self.alSource.position[0], self.alSource.position[1], self.alSource.position[2]

	async def setPosition(self, x: float, y: float, z: float):
		self.alSource.position=[x, y, z]
		await self._postEvent('positionUpdated',  x = x, y = y, z = z)

	@property
	def direction(self):
		return self.alSource.direction[0], self.alSource.direction[1], self.alSource.direction[2]

	async def setDirection(self, x: float, y: float, z: float):
		self.alSource.direction=[x, y, z]
		await self._postEvent('directionUpdated',  x = x, y = y, z = z)

	@property
	def pitch(self):
		return self.alSource.pitch*100

	async def setPitch(self, val: float):
		self.alSource.pitch=val/100
		await self._postEvent('pitchUpdated',  pitch = val)

	@property
	def direct(self):
		return self._direct


	async def enableDirect(self):
		self.alSource.relative=True
		self.alSource.direct_channels=True
		self._direct = True
		await self._postEvent('directEnabled')

	async def disableDirect(self):
		self.alSource.relative=False
		self.alSource.direct_channels=False
		self._direct = False
		await self._postEvent('directDisabled')

	@property
	def rolloffFactor(self):
		return self.alSource.rolloff_factor*100

	async def setRolloffFactor(self, val: float):
		self.alSource.rolloff_factor=val/100
		await self._postEvent('rolloffFactorUpdated',  rolloffFactor = val)

	@property
	def looping(self):
		return self.alSource.looping


	async def enableLooping(self):
		self.alSource.looping=True
		await self._postEvent('loopingEnabled')

	async def disableLooping(self):
		self.alSource.looping= False
		await self._postEvent('loopingDisabled')

	@property
	def gain(self):
		return self.alSource.gain*100


	async def setGain(self, val: float):
		self.alSource.gain=val/100
		await self._postEvent('gainUpdated', gain = val)

	@property
	def isPlaying(self):
		return self.alSource.state==cyal.SourceState.PLAYING

	@property
	def isPaused(self):
		return self.alSource.state == cyal.SourceState.PAUSED

	@property
	def isStopped(self):
		return self.alSource.state in [cyal.SourceState.INITIAL, cyal.SourceState.STOPPED,]

	async def play(self):
		if self.isPlaying: return
		if not self.playedOnce: self.playedOnce=True
		self.alSource.play()
		await self._postEvent('playing')

	async def stop(self):
		if  not self.isStopped: return self.alSource.stop()
		await self._postEvent('stopped')

	async def pause(self):
		if self.isPlaying: return self.alSource.pause()
		await self._postEvent('paused')

	async def _postEvent(self, event: str, **kwargs):
		await self.eventManager.postEvent('electrode.audio.sound.'+event, sound = self, **kwargs)