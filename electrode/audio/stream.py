from asyncio import sleep

import cyal

from electrode.audio.sound import Sound

class Stream(Sound):
	def __init__(self,  context: cyal.Context, sampleRate: int, channels: int, bufferSize: int = 1024, numberOfBuffers: int = 3, **kwargs):
		self.context = context
		self.bufferSize = bufferSize
		self.numberOfBuffers = numberOfBuffers
		self.sampleRate = sampleRate
		self.format = cyal.BufferFormat.MONO16 if channels==1 else cyal.BufferFormat.STEREO16
		self.alSource=context.gen_source()
		self.alSource.spatialize = True
		self.position=[0.0, 0.0, 0.0]
		self._direct = False
		self.playedOnce = False
		for key, value in kwargs.items():
			setattr(self, key, value)

	async def bufferData(self):
		self.seek(0)
		while self.streaming():
			await sleep(0.01)
			if self.alSource.buffers_processed > 0: self.alSource.unqueue_buffers(max = self.alSource.buffers_processed)
			if not self.alSource.buffers_queued < self.numberOfBuffers: continue
			buffs = self.context.gen_buffers(self.numberOfBuffers-self.alSource.buffers_queued)
			for buff in buffs: buff.set_data(self.read(), sample_rate = self.sampleRate, format = self.format)
			self.alSource.queue_buffers(*buffs)

	def seek(self, amount: int):
		pass

	def read(self):
		pass

	def streaming(self):
		pass