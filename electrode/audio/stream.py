from io import BytesIO
from asyncio import sleep

import cyal

from electrode.audio.sound import Sound

class stream(Sound):
	def __init__(self,  context: cyal.Context, dataStream: BytesIO,sampleRate: int, channels: int, bufferSize: int = 1024, numberOfBuffers: int = 3, **kwargs):
		self.context = context
		self.dataStream = dataStream
		self.bufferSize = bufferSize
		self.numberOfBuffers = numberOfBuffers
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
			if self.alSource.buffers_processed > 0: self.alSource.unqueue_buffers(max = self.alSource.buffers_processed)
			if not self.alSource.buffers_queued < self.numberOfBuffers: continue
			buffs = self.context.gen_buffers(self.numberOfBuffers-self.alSource.queued_buffers)
			for buff in buffs: buff.set_data(self.dataStream.read(self.bufferSize), format = self.format)
			self.alSource.queue_buffers(*buffs)