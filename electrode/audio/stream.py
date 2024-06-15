from io import BytesIO
from weakref import WeakSet
from asyncio import sleep

import cyal

from electrode.audio.sound import Sound

class stream(Sound):
	def __init__(self,  context: cyal.Context, dataStream: BytesIO,sampleRate: int, channels: int, bufferSize: int = 1024, **kwargs):
		self.context = context
		self.dataStream = dataStream
		self.bufferSize = bufferSize
		self.numberOfBuffers = 3
		self.buffers: WeakSet [cyal.buffer.Buffer] =  WeakSet()
		self.sampleRate = sampleRate
		self.format = cyal.BufferFormat.MONO16 if channels==1 else cyal.BufferFormat.STEREO16
		self.alSource=context.gen_source()
		self.alSource.spatialize = True
		self.position=[0.0, 0.0, 0.0]
		self._direct = False
		for key, value in kwargs.items():
			setattr(self, key, value)

	async def bufferData(self):
		self.dataStream.seek(0)
		while self.dataStream:
			await sleep(0.01)
			if len(self.buffers) < self.numberOfBuffers: self._getBuffers()
			for buff in self.buffers:
				buff.set_data(self.dataStream.read(self.bufferSize))

	def _getBuffers(self):
		buffersProcessed = self.alSource.buffers_processed
		if buffersProcessed>0:
			self.buffers.update([self.alSource.unqueue_buffers(buffersProcessed)])
		if len(self.buffers) < self.numberOfBuffers: self.buffers.update(self.context.gen_buffers(self.numberOfBuffers-len(self.buffers)))