"""
Keyboard input class for electrode.
"""
from pygame import KEYDOWN, KEYUP
from pygame import event as pgEvent
from .keyConstants import KeyConstants

class Keyboard:
	def __init__(self):
		self.heldKeys=set()
		self.lastKeyPressed=None
		self.lastKeyReleased=None
		self.keyConstants=KeyConstants

	def push(self):
		events=pgEvent.get()
		self.lastKeyPressed=None
		self.lastKeyReleased=None
		for event in events:
			if event.type==KEYUP:
				self.heldKeys.discard(event.key)
				self.lastKeyReleased=event.key
				continue
			if not event.type==KEYDOWN: continue
			if event.key not in self.heldKeys: self.lastKeyPressed=event.key
			self.heldKeys.add(event.key)

	def keyDown(self, keyCode):
		return keyCode in self.heldKeys

	def keyUp(self, keyCode):
		return key not in self.heldKeys

	def keyPressed(self, keyCode):
		return self.lastKeyPressed==keyCode

	def keyReleased(self, keycode):
		return self.lastKeyReleased==keycode