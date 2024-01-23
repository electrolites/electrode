"""
Event observer for electrode.
"""
from abc import ABC, abstractmethod

class observer(ABC):
	@abstractmethod
	async def trigger(event):
		pass