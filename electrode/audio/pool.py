"""
Electrodes Sound pool class.
"""
import os
import cyal
import soundfile
from electrode.audio.generators import sine, square, sawtooth, triangle, whiteNoise, brownNoise, pinkNoise, speech
from electrode.audio.pack import Pack
try:
	from electrode.audio.generators import gspeech
except ModuleNotFoundError:
	pass

class pool:
	def __init__(self, context: cyal.context, path: str, key: str = ""):
		self.context=context
		self.cache={}
		if path.endswith(".zip"):
			self.pack=Pack(path, key)
			self.path = ""
			return
		elif not os.path.isdir(path):
			raise ValueError(f"{path} is not a directory.")
		self.path=path
		if not self.path.endswith("/"): self.path+="/"

	def get(self, file: str):
		if not file in self.cache.keys(): self.cache[file]=self.getBufferFromFile(file)
		return self.cache[file]

	def getBufferFromFile(self, file: str):
		file=self.path+file
		if not hasattr(self, "pack"): fileObject=soundfile.SoundFile(file, 'r')
		elif file in self.pack.data.keys(): fileObject = soundfile.SoundFile(self.pack.data[file], 'r')
		format=cyal.BufferFormat.MONO16 if fileObject.channels==1 else cyal.BufferFormat.STEREO16
		buffer = self.context.gen_buffer()
		data=fileObject.read(dtype='int16').tobytes()
		fileObject.close()
		buffer.set_data(data, sample_rate=fileObject.samplerate, format=format)
		return buffer

	def generate(self, generatorType: str, *args, **kwargs):
		generator=0
		match generatorType:
			case "sine": generator=sine.Sine(*args, **kwargs)
			case "square": generator=square.Square(*args, **kwargs)
			case "sawtooth": generator = sawtooth.Sawtooth(*args, **kwargs)
			case "triangle": generator=triangle.Triangle(*args, **kwargs)
			case "whitenoise": generator=whiteNoise.WhiteNoise(*args, **kwargs)
			case "brownnoise": generator=brownNoise.BrownNoise(*args, **kwargs)
			case "pinknoise": generator = pinkNoise.PinkNoise(*args, **kwargs)
			case "speech": generator=speech.Speech(*args, **kwargs)
			case "gspeech":
				try: generator = gspeech.GSpeech(*args, **kwargs)
				except NameError: raise RuntimeError('You must install the gtts python package before using the GSpeech generator.')
		buffer=self.context.gen_buffer()
		format=cyal.BufferFormat.MONO16 if generator.channels==1 else cyal.BufferFormat.STEREO16
		buffer.set_data(generator.data, sample_rate=generator.sampleRate, format=format)
		return buffer


	def clear(self):
		self.cache.clear()
