"""
Brown noise generator for electrode.
"""
import numpy as np
from electrode.audio.generators.generator import Generator

class BrownNoise(Generator):
	def generate(self, length: float, rate: int = 44100, **kwargs):
		t = np.linspace(0, length, int(rate * length), endpoint=False)
		signal = np.cumsum(np.random.normal(scale=1/np.sqrt(rate), size=len(t)))
		signal -= np.mean(signal)
		signal /= np.max(np.abs(signal))
		signal= (signal * 32767).astype(np.int16).tobytes()
		return signal, rate, 1
