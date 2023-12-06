"""
Zone class for electrode.
"""
from coordinateContainer import CoordinateContainer

class zone(CoordinateContainer):
	def __init__(self, minX: int, maxX: int, minY: int, maxY: int, minZ: int, maxZ: int, text: str, speak=True):
		super().__init__(minX, maxX, minY, maxY, minZ, maxZ)
		self.text=text
		self.speak=speak