"""
Window class for electrode.
"""
from pygame import display, SHOWN, HIDDEN
from webcolors import name_to_rgb

class Window:
	def __init__(self, title: str):
		display.init()
		self._title=title
		self.size=(640, 480)
		self.pgRoot=None

	def show(self):
		self.pgRoot=display.set_mode(self.size, flags=SHOWN)
		display.set_caption(self._title)
		return self.pgRoot

	def hide(self):
		self.pgRoot=display.set_mode(self.size, flags=pygame.HIDDEN)
		return self.pgRoot

	@property
	def active(self):
		return display.get_active()

	def setColor(self, color: str):
		self.pgRoot.fill(name_to_rgb(color))