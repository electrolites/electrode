"""
Wall class for electrode.
"""
from surface import Surface

class Wall(surface):
	def __init__(self, minX: int, maxX: int, minY: int, maxY: int, minZ: int, maxZ: int, tile: str, transparent=False):
		super().__init__(minX, maxX, minY, maxY, minZ, maxZ,tile)
		self.transparent=transparent