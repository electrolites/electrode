"""
text to speech generator for electrode.
"""
import gtts
from io import BytesIO
import soundfile
from electrode.audio.generators.generator import Generator

class GSpeech(Generator):
	def generate(self, text: str, **kwargs):
		kw={}
		if "slow" in kwargs:  kw["slow"]= kwargs.get("slow")
		if "language" in kwargs: kw["lang"]= kwargs.get("language")
		if "tld" in kwargs: kw["tld"] = kwargs.get("tld")
		engine=gtts.gTTS(text, **kw)
		byo = BytesIO()
		engine.write_to_fp(byo)
		byo.seek(0)
		with soundfile.SoundFile(byo, 'r') as sfile:
			signal= sfile.read(dtype = 'int16')
			signal = signal.tobytes()
			return signal, sfile.samplerate, sfile.channels