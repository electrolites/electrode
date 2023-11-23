"""
Sound related commands for electrode.
"""

from audio.manager import Manager
from audio.group import Group 
from commands.command import Command
from commands.requirements import Requirements

class directSound(Command):
	def __init__(self, manager: Manager, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.runOnce=True
		self.Sound=None
		self.manager=manager
		self.requires=Requirements.soundManager

	def execute(self):
		self.sound=self.manager.newSound(*self.args, **self.kwargs)
		self.sound.direct=True

	def isRunning(self):
		if self.sound is not None:  return self.sound.isPlaying
		return False

class Sound(Command):
	def __init__(self, manager: Manager, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.manager=manager
		self.requires=Requirements.soundManager

	def execute(self):
		self.sound=self.manager.newSound(*self.args, **self.kwargs)

	def isRunning(self):
		if self.sound is not None:  return self.sound.isPlaying
		return False

class OneShotSound(Command):
	def __init__(self, manager: Manager, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.manager=manager
		self.requires=Requirements.soundManager

	def execute(self):
		self.sound=self.manager.newOneShotSound(*self.args, **self.kwargs)

	def isRunning(self):
		if self.sound is not None:  return self.sound.isPlaying
		return False

class SoundGroup(Command):
	def __init__(self, manager: Manager, *args, **kwargs):
		self.manager=manager
		super().__init__(*args, **kwargs)
		self.requires=Requirements.soundManager

	def execute(self):
		self.group=self.manager.newGroup(*self.args, **self.kwargs)

	def isRunning(self):
		if self.group.destroyed: return False
		return True

class GroupSound(Command):
	def __init__(self, group: Group, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.group=group

	def execute(self):
		self.sound=self.group.newSound(*self.args, **self.kwargs)

	def isRunning(self):
		if self.sound is not None:  return self.sound.isPlaying
		else: return False