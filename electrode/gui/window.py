"""
Window class for electrode.
"""
from pygame import display, SHOWN, HIDDEN

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