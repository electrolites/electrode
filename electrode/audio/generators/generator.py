"""
generator class for electrode.
"""

class Generator:
	def __init__(self, *args, **kwargs):
		"""
		Initializes the generator and sets up the appropriate values.
		Do not overwrite this function, overwrite generate instead
		"""
		self.data, self.sampleRate, self.channels=self.generate(*args, **kwargs)

	def generate(self, *args, **kwargs):
		"""
		The function that is called to generate the sound for this generator.
		Must return: audioData, sampleRate, numberOfChannels.
		"""
		raise NotImplementedError(f'all generater classes must implement a generate function. The object {self} does not.')