"""
text to speech generator for electrode.
"""
import pyttsx4
from io import BytesIO
import soundfile
from electrode.audio.generators.generator import Generator

class Speech(Generator):
	def generate(self, text: str, **kwargs):
		engine=pyttsx4.Engine()
		print(dir(engine.tts))
		bio = BytesIO()
		engine.save_to_file(text, bio, "w.wave")
		engine.runAndWait()
		signal = bio.getvalue()
		bio.seek(0)
		#with soundfile.SoundFile(bio) as f:
#			rate = f.samplerate
		bio.close()
		return signal, 22000, 1