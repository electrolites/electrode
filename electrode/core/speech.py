"""
Speech classes for electrode.
"""
from accessible_output3.outputs import auto

class speaker:
	def speak(self,text: str):
		raise RuntimeError("any speaker class must define a speak function")

class ttsSpeaker:
	def __init__(self):
		self.output=auto.Auto()

	def speak(self, text: str, interrupt=True): self.output.speak(text,interrupt)

class segmentSpeaker(speaker):
	def __init__(self, speechPath :str):
		self.speechPath=speechPath
		self.cue=[]

	def speak(self, text: str,interrupt=True):
		if interrupt=True: self.cue.clear()
		text=text.lower()
		werds=text.split(" ")
		self.cue.extend(werds)

	def loop(self):
		for c in self.cue:
			#put speaking code here
			self.cue.remove(c)

class Speech:
	def __init__(self, speechType=0, **kwargs):
		"""
		type 0=tts, type 1=speech segments.
		Provide speechPath argument if type one is selected.
		"""
		self.type=speechType
		if self.type==0: self.speakr=ttsSpeaker()
		elif self.type==1:
			if "SpeechPath" in kwargs.keys(): self.speakr=segmentSpeaker(kwargs["speechPath"])
			else: raise RuntimeError('If speechType is 1, than speechPath must be provided as a parameter.')
		else: raise RuntimeError(f'speechType must be 0 or 1. Got {self.type}')


	def speak(self, text: str, interrupt=True): self.speakr.speak(text, interrupt)