"""
Electrodes Sound pool class.
"""
import os
import array
import cyal
from pydub import AudioSegment
from pydub.utils import get_array_type

class pool:
	def __init__(self, context: cyal.context, path: str):
		self.context=context
		if not os.path.isdir(path):
			raise ValueError(f"{path} is not a directory.")
		self.path=path
		if not self.path.endswith("/"): self.path+="/"
		self.cache={}

	def get(self, file: str):
		if not file in self.cache.keys(): self.cache[file]=self.getBufferFromFile(file)
		return self.cache[file]

	def getBufferFromFile(self, file: str):
		file=self.path+file
		segment=AudioSegment.from_file(file)
		segment.set_sample_width(2)  
		format=cyal.BufferFormat.MONO16 if segment.channels==1 else cyal.BufferFormat.STEREO16
		buffer = self.context.gen_buffer()
		data=segment.raw_data
		buffer.set_data(data, sample_rate=segment.frame_rate, format=format)
		return buffer

	def clear(self):
		self.cache.clear()