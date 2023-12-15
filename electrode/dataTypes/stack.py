"""
Stack class for electrode.
"""
from collections import deque

class Stack:
	def __init__(self):
		self._container=deque()

	def push(self, data):
		self._container.append(data)

	def pop(self):
		return self._container.pop()

	def peek(self):
		return self._container[-1]

	@property
	def empty(self):
		return len(self._container)==0

	def __len__(self):
		return len(self._container)