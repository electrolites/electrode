"""
Queue class for electrode.
"""

from collections import deque

class Queue:
	def __init__(self):
		self._buffer=deque()

	def enQueue(self, data):
		self._buffer.appendleft(data)

	def deQueue(self):
		if self.empty: return
		return self._buffer.pop()

	def frunt(self):
		return self._buffer[-1]

	@property
	def empty(self):
		return len(self._buffer)==0

	def __len__(self):
		return len(self._buffer)