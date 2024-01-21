"""
text to speech generator for electrode.
"""
import gtts
from io import BytesIO
import soundfile
from electrode.audio.generators.generator import Generator

class GSpeech(Generator):
	def generate(self, text: str, **kwargs):
		engine=gtts.gTTS(text)
		byo = BytesIO()
		engine.write_to_fp(byo)
		byo.seek(0)
		signal, rate = soundfile.read(byo, dtype = 'int16')
		signal = signal.tobytes()
		return signal, rate, 1