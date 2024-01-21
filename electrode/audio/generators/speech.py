"""
text to speech generator for electrode.
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
		signal, rate = soundfile.read(tempname, dtype = 'int16')
		tfile.delete = True
		signal = signal.tobytes()
		return signal, rate, 1