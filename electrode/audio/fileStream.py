"""
Contains the file stream class for electrode.
"""

from cyal import Context
from soundfile import SoundFile

from .stream import Stream

class FileStream(Stream):
	def __init__(self, context: Context, fileObject: SoundFile, bufferSize: int = 1024, numberOfBuffers: int = 3, **kwargs):
		self.fileObject = fileObject
		super().__init__(context, fileObject.samplerate, fileObject.channels, bufferSize= bufferSize, numberOfBuffers = numberOfBuffers, **kwargs)

	def seek(self, amount: int):
		return self.fileObject.seek(amount)

	def read(self):
		return self.fileObject.read(self.bufferSize, dtype='int16').tobytes()

	def streaming(self):
		return self.fileObject.tell()<len(self.fileObject)