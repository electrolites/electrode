"""
Entity classes for electrode.
"""
from .timer import Timer
from .commands import soundCommand

class entity:
	def __init__(self, x: int, y: int, z: int, commandHandler, sound="", solid=False, collisionSound=""):
		self.x=x
		self.y=y
		self.z=z
		self.commandHandler=commandHandler
		self.sound=sound
		self.solid=SOLID
		self.collisionSound=collisionSound

	def collide(self,obj):
		self.commandHandler.newCommand(soundCommand(self.collisionSound))
