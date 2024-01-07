"""
Keyboard input class for electrode.
"""
from pygame import KEYDOWN, KEYUP
from pygame import event as pgEvent
from .keyConstants import KeyConstants
from electrode.core.timer import Timer

class Keyboard:
	def __init__(self):
		self.heldKeys={}
		self.lastKeyPressed=None
		self.lastKeyReleased=None
		self.keyConstants=KeyConstants

	def push(self):
		events=pgEvent.get()
		self.lastKeyPressed=None
		self.lastKeyReleased=None
		for event in events:
			if event.type==KEYUP:
				self.heldKeys.pop(event.key)
				self.lastKeyReleased=event.key
				continue
			if not event.type==KEYDOWN: continue
			if event.key not in self.heldKeys.keys(): self.lastKeyPressed=event.key
			self.heldKeys[event.key]={"timer":Timer()}

	def keyDown(self, keyCode):
		return keyCode in self.heldKeys

	def keyUp(self, keyCode):
		return keyCode not in self.heldKeys

	def keyPressed(self, keyCode):
		return self.lastKeyPressed==keyCode

	def keyReleased(self, keycode):
		return self.lastKeyReleased==keycode

	def keyHolding(self, keycode, delay=500, repeat=50):
		if not self.keyDown(keycode): return False
		infoDict=self.heldKeys.get(keycode)
		t=infoDict.get("timer")
		if "lastDelayPassed" in infoDict:
			if infoDict.get("lastDelayPassed")>=delay and t.time>=repeat:
				t.restart()
				infoDict["lastDelayPassed"]=delay
				return True
		if t.time>=delay:
			infoDict["lastDelayPassed"]=delay
			t.restart()
			return True
		return False