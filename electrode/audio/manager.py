"""
Sound management classes for Electrode.
"""

from asyncio import create_task
from itertools import chain

from typing import Coroutine, Tuple

import cyal

from .pool import pool as Pool
from .sound import Sound
from .stream import Stream
from .fileStream import FileStream

class Manager:
	def __init__(self, path: str, eventManager, key: str = "",  device: cyal.Device | None=None, context: cyal.Context | None=None):
		self.device = device or cyal.Device()
		self.context=context or cyal.Context(self.device, make_current=True, hrtf_soft=1)
		self.alListener=self.context.listener
		self.alListener.orientation = [0.0, 1.0, 0.0, 0.0, 0.0, 1.0]
		self.alListener.position = [0, 0, 0]
		self.pool=Pool(self.context, path, key = key)
		self.oneShotSounds: list[Sound]=[]
		self.sounds: list[Sound]=[]
		self.streams: list[Stream] = []
		self.eventManager = eventManager

	async def addSound(self, event):
		if event['oneShot']==True:
			if event['sound'].looping==True: raise ValueError("Looping must be False if oneShot is true.")
			self.oneShotSounds.append(event['sound'])
		else: self.sounds.append(event['sound'])

	async def addStream(self, event):
		self.streams.append(event['stream'])

	async def triCleanOneShots(self, event: dict):
		for s in self.oneShotSounds:
			if s.isStopped: self.oneShotSounds.remove(s)
		await self.eventManager.postEvent('electrode.audioManager.triedCleanOneShots')

	async def forceCleanOneShots(self, event: dict):
		for s in self.oneShotSounds:
			if not s.isStopped: await s.stop()
		self.oneShotSounds.clear()
		await self.eventManager.postEvent('electrode.audioManager.forcedCleanOneShots')

	async def triCleanAll(self, event):
		await self.eventManager.postEvent('electrode.command.audioManager.triCleanOneShots')
		for s in self.sounds:
			if s.isStopped: self.sounds.remove(s)
		self.eventManager.postEvent('electrode.audioManager.triedCleanAll')

	async def forceCleanAll(self):
		await self.eventManager.postEvent('electrode.command.audioManager.forceCleanOneShots')
		await self.eventManager.waitForEvent('electrode.audioManager.triedCleanOneShots')
		for s in self.sounds:
			if not s.isStopped: await s.stop()
		self.sounds.clear()
		await self.eventManager.postEvent('electrode.audioManager.forcedCleanAll')

	async def changeListenerPosition(self, event: dict):
		self.alListener.position = [event['x'], event['z'], event['y']]
		await self.eventManager.postEvent('electrode.audioManager.listenerPositionChanged', x = self.alListener.position[0], y = self.alListener.position[2]*-1, z = self.alListener.position[1])

	async def changeListenerX(self, event: dict):
		await self.eventManager.postEvent('electrode.command.changeListenerPosition', x = event['x'], y = self.alListener.position[2]*-1, z = self.alListener.position[1])

	async def changeListenerY(self, event: dict):
		await self.eventManager.postEvent('electrode.command.changeListenerPosition', x = self.alListener.position[0], y = event['y'], z = self.alListener.position[1])

	async def changeListenerZ(self, event: dict):
		await self.eventManager.postEvent('electrode.command.changeListenerPosition', x = self.alListener.position[0], y = self.alListener.position[2]*-1, z = event['z'])

	async def _setUpInternalEvents(self):
		eventPrefix = 'electrode.audio.manager.'
		soundEventPrefix = 'electrode.audio.sound.'
		streamEventPrefix = 'electrode.audio.stream.'
		commandPrefix = 'electrode.command.audioManager.'
		events = {
			eventPrefix+'listenerPositionChanged': {'x': int, 'y': int, 'z': int},
			commandPrefix+'changeListenerPosition': {'x': int, 'y': int, 'z': int},
			commandPrefix+'changeListenerX': {'x': int},
			commandPrefix+'changeListenerY': {'y': int},
			commandPrefix+'changeListenerZ': {'z': int},
			commandPrefix+'addSound': {'sound': Sound, 'oneShot': bool},
			commandPrefix+'addStream': {'stream': Stream},
			eventPrefix+'triedCleanOneShots': {},
			eventPrefix+'forcedCleanOneShots': {},
			eventPrefix+'triedCleanAll': {},
			eventPrefix+'forcedCleanAll': {},
			commandPrefix+'tryCleanOneShots': {},
			commandPrefix+'forceCleanOneShots': {},
			commandPrefix+'tryCleanAll': {},
			commandPrefix+'forceCleanAll': {},
			soundEventPrefix+'stopped': {'sound': Sound},
			soundEventPrefix+'paused': {'sound': Sound},
			soundEventPrefix+'playing': {'sound': Sound},
			soundEventPrefix+'gainUpdated': {'sound': Sound, 'gain': float},
			soundEventPrefix+'rolloffFactorUpdated': {'sound': Sound, 'rolloffFactor': float},
			soundEventPrefix+'pitchUpdated': {'sound': Sound, 'pitch': float},
			soundEventPrefix+'directEnabled': {'sound': Sound},
			soundEventPrefix+'directDisabled': {'sound': Sound},
			soundEventPrefix+'directionUpdated': {'sound': Sound, 'x': float, 'y': float, 'z': float},
			soundEventPrefix+'positionUpdated': {'sound': Sound, 'x': float, 'y': float, 'z': float},
		}
		for name, structure in events.items():
			await self.eventManager.register(name, **structure)
		await self._subscribeToInternalEvents()

	async def _subscribeToInternalEvents(self):
		eventPrefix = 'electrode.audio.manager.'
		commandPrefix = 'electrode.command.audioManager.'
		self.eventManager.subscribe(commandPrefix+'changeListenerPosition', self.changeListenerPosition)
		self.eventManager.subscribe(commandPrefix+'changeListenerX', self.changeListenerX)
		self.eventManager.subscribe(commandPrefix+'changeListenerY', self.changeListenerY)
		self.eventManager.subscribe(commandPrefix+'changeListenerZ', self.changeListenerZ)
		self.eventManager.subscribe(commandPrefix+'addSound', self.addSound)
		self.eventManager.subscribe(commandPrefix+'addStream', self.addStream)
		self.eventManager.subscribe(commandPrefix+'triCleanOneShots', self.triCleanOneShots)
		self.eventManager.subscribe(commandPrefix+'forceCleanOneShots', self.forceCleanOneShots)
		self.eventManager.subscribe(commandPrefix+'triCleanAll', self.triCleanAll)
		self.eventManager.subscribe(commandPrefix+'forceCleanAll', self.forceCleanAll)