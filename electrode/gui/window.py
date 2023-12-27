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
		self.pgRoot=display.set_mode(self.size, flags=HIDDEN)
		return self.pgRoot

	@property
	def active(self):
		return display.get_active()

	def setColor(self, color: str):
		self.pgRoot.fill(name_to_rgb(color))
		display.flip()

	@property
	def fullScreen(self):
		if display.is_fullscreen(): return True
		return False

	@fullScreen.setter
	def fullScreen(self, val: bool):
		if val==True:
			if self.fullScreen==True: return
			display.toggle_fullscreen()
		if self.fullScreen==False: return
		display.toggle_fullscreen()

	@property
	def title(self):
		return self._title

	@title.setter
	def title(self, val: int):
		self._title=val
		display.set_caption(val)