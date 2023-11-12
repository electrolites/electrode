"""
Seen commands for electrode.
"""
from seen.manager import Manager
from seen.seen import Seen
from seen.states import States
from commands.command import Command

class newSeen(Command):
	def __init__(self, seenManager: Manager, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.manager=seenManager
		self.seen=None

	def execute(self):
		self.manager.newSeen(*self.args, **self.kwargs)

	def isRunning(self):
		return self.seen.state==States.ENTERD if self.seen is not None else False

class runSeen(Command):
	def __init__(self, seenManager: Manager, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.manager=seenManager
		self.seen=None

	def execute(self):
		self.seen=self.manager.runSeen(*self.args, **self.kwargs)

	def isRunning(self):
		return self.seen.state==States.ENTERD if self.seen is not None else False


class runNewSeen(Command):
	def __init__(self, seenManager: Manager, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.manager=seenManager
		self.seen=None

	def execute(self):
		self.seen=self.manager.runNewSeen(*self.args, **self.kwargs)

	def isRunning(self):
		return self.seen.state==States.ENTERD if self.seen is not None else False


class exitSeen(Command):
	def __init__(self, seenManager: Manager, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.manager=seenManager
		self.seen=None

	def execute(self):
		self.seen=self.manager.exitSeen(*self.args, **self.kwargs)

	def isRunning(self):
		return self.seen.state==States.ENTERD if self.seen is not None else False

class popSeen(Command):
	def __init__(self, seenManager: Manager, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.manager=seenManager
		self.seen=None

	def execute(self):
		self.seen=self.manager.popSeen(*self.args, **self.kwargs)

	def isRunning(self):
		return self.seen.state==States.ENTERD if self.seen is not None else False