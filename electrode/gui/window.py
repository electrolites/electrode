"""
Window class for electrode.
"""
import pygame

class Window:
	def __init__(self, title: str):
		pygame.init()
		self._title=title
		self.size=(640, 480)
		self.pgRoot=None

	def show(self):
		self.pgRoot=pygame.display.set_mode(self.size)
		pygame.display.set_caption(self._title)
		return self.pgRoot

	