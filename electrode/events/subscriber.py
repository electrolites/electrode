"""
Subscriber container for electrode.
"""

from typing import Coroutine
from dataclasses import dataclass

@dataclass(order = True)
class Subscriber:
	"""
	Data class holding required information about a subscriber in the electrode event class.
	"""
	Callback: Coroutine
	requirements: dict