"""
Pink noise generator for electrode.
"""
import numpy as np
from electrode.audio.generators.generator import Generator

class PinkNoise(Generator):
	def generate(self, length: float, rate: int = 44100, **kwargs):
		signal = np.random.uniform(-1, 1, int(rate * length))
		signal = self.pinkFilter(signal)
		signal /= np.max(np.abs(signal))
		signal= (signal * 32767).astype(np.int16).tobytes()
		return signal, rate, 1

	def pinkFilter(self, data):
		numSamples = len(data)
		pinkData = np.zeros(numSamples)
		# Pink noise filter coefficients
		b0 = 0.02109238
		b1 = -0.07113478
		b2 = 0.68873558
		b3 = 0.31077298
		b4 = 0.04798256
		for i in range(numSamples):
			pinkData[i] = b0 * data[i]
			if i > 0:
				pinkData[i] += b1 * data[i - 1]
			if i > 1:
				pinkData[i] += b2 * data[i - 2]
			if i > 2:
				pinkData[i] += b3 * data[i - 3]
			if i > 3:
				pinkData[i] += b4 * data[i - 4]
		return pinkData