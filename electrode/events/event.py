"""
Event class for electrode.
"""

import asyncio
from collections import defaultdict
from typing import Any, Coroutine, Protocol

from electrode.events.errors import eventExistsError, eventMissingError, invalidEventError

class eventManager:
	"""
	Class for subscribing to, registering,  and unregistering events
	"""
	async def __init__(self):
		"""
		Initializes the event manager.
		"""
		self.subscribers = defaultdict(list)
		self.registered={}

	async def register(self, event: str, structure: Protocol):
		"""
		registers an event, setting up its required data.

		:param event: The name of the event to register
		:type event: str
		:param structure: The required data for the event.
		:type structure: Protocol
		"""
		if event in self.registered.keys(): raise eventExistsError(event, self.registered[event], structure)
		self.registered[event] = structure

	async def subscribe(self, event: str, callBack: Coroutine):
		"""
		Subscribes to an event.

		:param event: The name of the event to subscribe to.
		:type event: str
		:param callBack: The function that is awaited upon the execution of the event.
		:type callBack: Coroutine
		"""
		if event not in self.registered.keys(): raise eventMissingError(f'The event {event} does not exist.', event)
		self.subscribers[event].append(callBack)

	async def unregister(self, event: str):
		"""
		unregisters an event, the event and all it's callBacks.

		:param event: The name of the event to unregister
		:type event: str
		"""
		self.registered.pop(event)
		self.subscribers.pop(event)

	async def postEvent(self, event: str, data: Any) -> None:
		"""
		Posts an event to its subscribers.

		:param event: The name of the event to post.
		:type event: str
		:param data: The extra data to go alon with the event.
		:type data: Any
		"""
		if event not in self.registered.keys(): raise eventMissingError(f'The event {event} does not exist.', event)
		if not isinstance(data, self.registered[event]): raise invalidEventError(f'The event {event} did not matche its registered protocol.', event)
		if event not in self.subscribers.keys(): return
		await asyncio.gather(*[e(data) for e in self.subscribers[event]])