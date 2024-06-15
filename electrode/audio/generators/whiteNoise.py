"""
White noise generator for electrode.
"""
import numpy as np
from electrode.audio.generators.generator import Generator

class WhiteNoise(Generator):
	def generate(self, length: float, rate: int = 44100, **kwargs):
		signal = np.random.uniform(-1, 1, int(rate * length))
		signal= (signal * 32767).astype(np.int16).tobytes()
		return signal, rate, 1
