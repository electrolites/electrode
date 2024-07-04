"""
Contains the main functions and loop for electrode.
"""

import asyncio
import time
from typing import Callable

from audio.manager import Manager as AudioManager
from core.enumbs import CreateEnum as CoreCreateEnum
from core import factories as CoreFactories
from events.manager import Manager as EventManager
from scene.manager import Manager as SceneManager

class Electrode:
	def __init__(self, startCallBack: Callable):
		"""
		initializes the main electrode class.
		"""
		self.eventManager = EventManager()
		self.sceneManager = SceneManager()
		self._audioManagerFactory = CoreFactories.audioManagerFactory(self.eventManager)
		self.translator = None
		self.window = None
		self.AsyncLoop = asyncio.get_event_loop()
		self._waitingForEventRegistration = True
		self.AsyncLoop.create_task(self._registerInternalEvents())
		self.startCallBack = startCallBack

	async def _registerInternalEvents(self):
		events = await Electrode.genorateBuiltInEvents()
		for name, eventStructure in events:
			await self.eventManager.register(event = name, structure = eventStructure)
		self._waitingForEventRegistration = False

	async def _subscribeToInternalEvents(self):
		while self._waitingForEventRegistration:
			await asyncio.sleep(0.0003)
		await self.eventManager.subscribe('electrode.command.initializeAudioManager', self._initializeAudioManager)
		await self.eventManager.subscribe('electrode.internal.subscriptionsComplete', self._completeInitialization)
		await self.eventManager.subscribe('electrod.general.start', self.startCallBack)
		await self.eventManager.postEvent('electrode.internal.subscriptionsComplete')

	async def _completeInitialization(self, event):
		await self.eventManager.unregister('electrode.internal.subscriptionsComplete')
		await self.eventManager.postEvent('electrode.general.start', time = time.time())

	@classmethod
	async def genorateBuiltInEvents(cls):
		return {
			'electrode.general.start': {'time': time.time},
			'electrode.internal.subscriptionsComplete': {},
			'electrode.Command.initializeAudioManager': {'path': str, 'key': str},
			'electrode.audioManager.initialized': {'audioManager', AudioManager}
		}