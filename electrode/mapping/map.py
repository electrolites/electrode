"""
mapping classes for electrode.
"""
#imports:
from itertools import chain
from coordinateContainer import CoordinateContainer
from surface import Surface
from surface import VanishingSurface
from wall import Wall
from zone import zone

class Map(CoordinateContainer):
	def __init__(self, minX=0, maxX=0, minY=0, maxY=0, minZ=0, maxZ=0, dynamic=True):
		super().__init__(minX, maxX, minY, maxY, minZ, maxZ)
		self.dynamic=dynamic
		self.objects=[]
		self.dynamicObjects=[]
		self.dynamicTypes=[wall,surface,vanishingSurface]

	def get(self, objectType):
		if objectType in self.dynamicTypes and self.dynamic: return list(filter(lambda item: isinstance(item, objectType), self.dynamicObjects))
		return list(filter(lambda item: isinstance(item, objectType), self.objects))

	def add(self, obj, minX: int, maxX: int, minY: int, maxY: int, minZ: int, maxZ: int, *args, **kwargs):
		if not self.dynamic or not obj in self.dynamicTypes: self.objects.append(obj(minX, maxX, minY, maxY, minZ, maxZ,*args,**kwargs))
		else:
			self.dynamicObjects.append(obj(minX, maxX, minY, maxY, minZ, maxZ,*args,**kwargs))
			self.dynamiclyResize()

	def remove(self, obj, minX: int, maxX: int, minY: int, maxY: int, minZ: int, maxZ: int, extras={}):
		for o in self.get(obj):
			if not o.minX==minX: continue
			if not o.maxX==maxX: continue
			if not o.minY==minY: continue
			if not o.maxY==maxY: continue
			if not o.minZ==minZ: continue
			if not o.maxZ==maxZ: continue
			for k, v in extras.items():
				if not hasattr(o,k): continue
				if not getattr(o,k)==v: continue
			if not self.dynamic or o not in self.dynamicTypes: self.objects.remove(o)
			else: self.dynamicObjects.remove(o)
			break


	def resize(self, minX: int, maxX: int, minY: int, maxY: int, minZ: int, maxZ: int):
		self.minX=minX
		self.maxX=maxX
		self.minY=minY
		self.maxY=maxY
		self.minZ=minZ
		self.maxZ=maxZ

	def dynamiclyResize(self):
		if self.dynamic==False: raise RuntimeError("Can not dynamicly resize when the dynamic attribute is set to false.")
		minX=min(self.dynamicObjects,key=lambda obj: obj.minX).minX
		maxX=max(self.dynamicObjects,key=lambda obj: obj.maxX).maxX
		minY=min(self.dynamicObjects,key=lambda obj: obj.minY).minY
		maxY=max(self.dynamicObjects,key=lambda obj: obj.maxY).maxY
		minZ=min(self.dynamicObjects,key=lambda obj: obj.minZ).minZ
		maxZ=max(self.dynamicObjects,key=lambda obj: obj.maxZ).maxZ
		self.resize(minX, maxX, minY, maxY, minZ, maxZ)

	def getTile(self, x, y, z):
		for s in reversed(self.get(vanishingSurface)):
			if s.isHere(x,y,z) and s.active: return s.tile
		for s in reversed(self.get(surface)):
			if s.isHere(x,y,z): return s.tile

	def getZone(self,x: int, y: int, z: int):
		for zo in reversed(self.get(zone)):
			if zo.isHere(x,y,z): return zo.text, zo.speak

	def onWall(self, x: int, y: int, z: int):
		for w in reversed(self.get(wall)):
			if w.isHere(x,y,z): return True
		return False

	def getWall(self, x: int, y: int, z: int):
		wallTile=None
		for w in reversed(self.get(wall)):
			if w.isHere(x,y,z): return w.tile

	def lock(self, obj):
		if not hasattr(obj,"x") or not hasattr(obj,"y") or not hasattr(obj,"z"): raise RuntimeError("Any object passed to map.lock must have an x, y, and z atribute.")
		if self.isHere(obj.x,obj.y,obj.z): return
		if obj.x>self.maxX: obj.x=self.maxX
		elif obj.x<self.minX: obj.x=self.minX
		if obj.y>self.maxY: obj.y=self.maxY
		elif obj.y<self.minY: obj.y=self.minY
		if obj.z>self.maxZ: obj.z=self.maxZ
		elif obj.z<self.minZ: obj.z=self.minZ