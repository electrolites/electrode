"""
Seen manager class for electrode.
"""
from seen import Seen
from states import States
	

class Manager:
	def __init__(self):
		self.stack: list[Seen]=[]
		self.latestSeen=None
		self.runningSeen=None

	def newSeen(self, seen: Seen, **kwargs):
		seen.stack=self.stack
		seen.parent=self.latestSeen
		self.latestSeen=seen
		return seen.append(seen, **kwargs)

	def runSeen(self, name: str, **kwargs):
		seen=None
		seen=self.getSeen(name)
		if seen==None: raise RuntimeError(f'seen {name} was not found in the seen manager {self}.')
		self.runningSeen=seen
		if seen.parent is not None:
			if seen.parent.state!=States.EXITED: seen.parent.onExit()
			seen.onEnter(**kwargs)
		return seen

	def runNewSeen(self, seen: Seen):
		self.newSeen(seen)
		return self.runSeen(seen.name)

	def exitSeen(self, name: str, **kwargs):
		seen=None
		seen=self.getSeen(name)
		if seen==None: raise RuntimeError(f'seen {name} was not found in the seen manager {self}.')
		seen.onExit(**kwargs)
		if seen.parent is not None:
			if seen.parent.state!=States.ENTERD: self.run(seen.parent.name)
		return seen

	def popSeen(self, seen: Seen):
		if seen not in self.stack: raise RuntimeError(f'seen {seen} with name {seen.name} was not found in the seen manager {self}.')
		if seen==self.latestSeen and seen.parent is not None: self.latestSeen=seen.parent
		return Seen.pop(seen)

	def getSeen(self,name: str):
		for s in self.stack:
			if s.name==name: return s