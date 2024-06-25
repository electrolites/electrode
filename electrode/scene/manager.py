"""
Scene manager class for electrode.
"""
from scene import Scene
from states import States
	

class Manager:
	def __init__(self):
		self.stack: list[Scene]=[]
		self.latestScene=None
		self.runningScene=None

	def newScene(self, scene: Scene, **kwargs):
		scene.stack=self.stack
		scene.parent=self.latestScene
		self.latestScene=scene
		return scene.append(scene, **kwargs)

	def runScene(self, name: str, **kwargs):
		scene=None
		scene=self.getScene(name)
		if scene==None: raise RuntimeError(f'scene {name} was not found in the scene manager {self}.')
		self.runningScene=scene
		if scene.parent is not None:
			if scene.parent.state!=States.EXITED: scene.parent.onExit()
			scene.onEnter(**kwargs)
		return scene

	def runNewScene(self, scene: Scene):
		self.newScene(scene)
		return self.runScene(scene.name)

	def exitScene(self, name: str, **kwargs):
		scene=None
		scene=self.getScene(name)
		if scene==None: raise RuntimeError(f'scene {name} was not found in the scene manager {self}.')
		scene.onExit(**kwargs)
		if scene.parent is not None:
			if scene.parent.state!=States.ENTERD: self.run(scene.parent.name)
		return scene

	def popScene(self, scene: Scene):
		if scene not in self.stack: raise RuntimeError(f'scene {scene} with name {scene.name} was not found in the scene manager {self}.')
		if scene==self.latestScene and scene.parent is not None: self.latestScene=scene.parent
		return Scene.pop(scene)

	def getScene(self,name: str):
		for s in self.stack:
			if s.name==name: return s