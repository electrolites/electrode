"""
scene class for electrode.
"""
from states import States

class Scene:
	#when overwriting any function in this class that does not contain a not implemented rase, make sure you call the super classes version of that function.
	def __init__(self, name: str="scene"):
		self.parent=None
		self.stack=[]
		self.name=name
		self.state=States.INITIAL

	def onPush(self):
		#this function is called when ever this scene is pushed on to the managers stac. Initialize all resources here.
		self.state=States.PUSHED

	def onEnter(self):
		#Called when this scene has been told to run bye the manager. Start the actions that this scene does here.
		self.state=States.ENTERD

	def onExit(self):
		#Called when this scene has been told to exit bye the manager. Close the actions that this scene does here.
		self.state=States.EXITED

	def onPop(self):
		#Called when this scene is popped off the Managers stack. Destroy all resources related to this scene  here.
		self.state=States.POPPED

	def append(self, scene=None):
		scene=scene or self
		if not scene==self: scene.parent=self
		scene.onPush()
		return self.stack.append(scene)

	def getRootScene(self):
		return self.parent.getRootScene() if self.parent is not None else self

	def pop(self, scene=None):
		scene=scene or self
		if not scene.state==States.EXITED: scene.onExit()
		scene.onPop()
		return self.stack.pop(self.stack.index(scene))

	def popAndReplace(self, scene=None):
		scene=scene or self
		for s in self.stack: s.pop()
		scene.append()