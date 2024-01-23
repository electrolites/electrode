"""
Text to speech generator for electrode.
"""
import pyttsx4
from io import BufferedReader, BytesIO
import tempfile
import soundfile
from electrode.audio.generators.generator import Generator

class Speech(Generator):
	def generate(self, text: str, **kwargs):
		tfile=tempfile.NamedTemporaryFile('r')
		tempname = tfile.name
		tfile.close()
		engine=pyttsx4.Engine()
		engine.save_to_file(text, tempname, )
		engine.runAndWait()
		with soundfile.SoundFile(tempname, 'r') as sfile:
			signal = sfile.read(dtype = 'int16')
			tfile.delete = True
			signal = signal.tobytes()
			return signal, sfile.samplerate, sfile.channels