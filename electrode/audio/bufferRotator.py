"""
Simple audio buffer rotation class for electrode.
"""
import cyal

class BufferRotator:
	def __init__(self, context: cyal.Context, alSource: cyal.Source):
		self.source = alSource
		self.context = context
		self.buffering = False
		self.buffers: list[cyal.Buffer] = []

	def startRotating(self):
		self.buffering = True
		while self.buffering:
			