"""
Coordinate container class for electrode.
"""

class CoordinateContainer:
	def __init__(self, minX: int, maxX: int, minY: int, maxY: int, minZ: int, maxZ: int):
		self.minX=minX
		self.maxX=maxX
		self.minY=minY
		self.maxY=maxY
		self.minZ=minZ
		self.maxZ=maxZ

	def isHere(self, x: int, y: int, z: int):
		if x<self.minX: return False
		if x>self.maxX: return False
		if y<self.minY: return False
		if y>self.maxY: return False
		if z<self.minZ: return False
		if z>self.maxZ: return False
		return True