"""
Triangle generator for electrode.
"""
import numpy as np
from electrode.audio.generators.generator import Generator

class Triangle(Generator):
	def generate(self, frequency: float, length: float, rate: int = 44100, sweepFrequency: float | None = None, **kwargs):
		t = np.linspace(0, length, int(rate * length), endpoint=False)
		if sweepFrequency is not None:
			signal = 2 * np.abs(t * (frequency + (sweepFrequency - frequency) * t / length) % 1 - 0.5) * 2 - 1
		else:
			signal = 2 * np.abs(t * frequency % 1 - 0.5) * 2 - 1
		signal = (signal * 32767).astype(np.int16).tobytes()
		return signal, rate, 1