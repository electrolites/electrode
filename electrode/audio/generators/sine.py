"""
sine wave generator for electrode.
"""
import numpy as np
from electrode.audio.generators.generator import Generator

class Sine(Generator):
	def generate(self, frequency: float, length: float, rate: int = 44100, sweepFrequency: float | None = None, **kwargs):
		t = np.linspace(0, length, int(rate * length), endpoint=False)
		if sweepFrequency is not None:
			signal = 0.5 * np.sin(2 * np.pi * np.linspace(frequency, sweepFrequency, len(t)) * t)
		else:
			signal = 0.5 * np.sin(2 * np.pi * frequency * t)
		signal = (signal * 32767).astype(np.int16).tobytes()
		return signal, rate, 1