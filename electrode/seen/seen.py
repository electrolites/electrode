"""
seen class for electrode.
"""
from states import States

class Seen:
	#when overwriting any function in this class that does not contain a not implemented rase, make sure you call the super classes version of that function.
	def __init__(self, name: str="seen"):
		self.parent=None
		self.stack=[]
		self.name=name
		self.state=States.INITIAL

	def onPush(self):
		#this function is called when ever this state is pushed on to the managers stac. Initialize all resources here.
		self.state=States.PUSHED

	def onEnter(self):
		#Called when this seen has been told to run bye the manager. Start the actions that this seen does here.
		self.state=States.ENTERD


	def onExit(self):
		#Called when this seen has been told to exit bye the manager. Close the actions that this seen does here.
		self.state=States.EXITED

	def onPop(self):
		#Called when this seen is popped off the Managers stack. Destroy all resources related to this seen  here.
		self.state=States.POPPED

	def append(self, seen=None):
		seen=seen or self
		if not seen==self: seen.parent=self
		seen.onPush()
		return self.stack.append(seen)

	def getRootSeen(self):
		return self.parent.getRootSeen() if self.parent is not None else self

	def pop(self, seen=None):
		seen=seen or self
		if not seen.state==States.EXITED: seen.onExit()
		seen.onPop()
		return self.stack.pop(self.stack.index(seen))

	def popAndReplace(self, seen=None):
		seen=seen or self
		for s in self.stack: s.pop()
		seen.append()