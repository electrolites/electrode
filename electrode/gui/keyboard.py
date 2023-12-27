"""
Keyboard input class for electrode.
"""
from pygame import event, key, KEYDOWN, KEYUP
from keyConstants import KeyConstants

class Keyboard:
	def __init__(self):
		self.pgRoot=key
		self.heldKeys=set()
		self.lastKeyPressed=None
		self.lastKeyReleased=None
		self.keyConstants=KeyConstants

	def push(self):
		events=event.get()
		for event in events:
			if event.type==KEYUP:
				self.heldKeys.discard(event.key)
				self.lastKeyReleased=event.key
				continue
			if not event.type==KEYDOWN: continue
			if event.key not in self.heldKeys: self.lastKeyPressed=event.key
			self.heldKeys.add(event.key)

	def KEYDOWN(self, keyCode):
		return keyCode in self.heldKeys

	def keyUp(self, keyCode):
		return key not in self.heldKeys

	def keyPressed(self, keyCode):
		return self.lastKeyPressed==keyCode

	def keyReleased(self, keycode):
		return self.lastKeyReleased==keycode