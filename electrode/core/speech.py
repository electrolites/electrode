"""
Speech classes for electrode.
"""
from accessible_output3 import outputs

class Speech:
	"""
	Class for speaking and brailling output.
	"""
	def __init__(self, braille: bool = True, outputType: str = "auto"):
		"""
		initialize the speech class.

		:param braille: Sets if text should be brailled as well as being spoken, defaults to True
		:type braille: bool, optional
		:param outputType: Sets the type of output, nvda, jaws, sapi, voiceover, ns, zdsr, speechd, espeak, dolphin, pctalker, systemaccess, windoweyes, or auto, defaults to "auto"
		:type outputType: str, optional
		"""
		self.output = self._getOutput(outputType)

	@classmethod
	def _getOutput(self, outputType: str):
		"""
		Gets the output from the provided string.

		:param outputType: The type of output, nvda, jaws,  sapi, voiceover, ns, zdsr, speechd, espeak, dolphin, pctalker, systemaccess, windoweyes, or auto
		:type outputType: str
		"""
		match outputType:
			case "auto": return outputs.auto.Auto()
			case "dolphin": return outputs.dolphin.Dolphin()
			case "espeak": return outputs.e_speak.ESpeak()
			case "jaws": return outputs.jaws.Jaws()
			case "mac", "mackintalk", "ns", "nsspeech": return outputs.nsspeechsynthesizer.MacSpeech()
			case "nvda": return outputs.nvda.NVDA()
			case "pctalker": return outputs.pc_talker.PCTalker()
			case "sapi", "sapi5": return outputs.sapi5.SAPI5()
			case "speechd", "speech-dispatcher", "speechdispatcher": return outputs.speech_dispatcher.SpeechDispatcher()
			case "systemaccess": return outputs.system_access.SystemAccess()
			case "voiceover": return outputs.voiceover.VoiceOver()
			case "windoweyes": return outputs.window_eyes.WindowEyes()
			case "zdsr": return outputs.zdsr.ZDSR()

	def speak(self, text: str, interrupt: bool = True):
		"""
		speaks the given text with the selected synthesizer.

		:param text: The text to be spoken.
		:type text: str
		:param interrupt: Sets if the spoken text should interrupt the currently speaking text, defaults to True
		:type interrupt: bool, optional
		"""
		self.output.speak(text, interrupt= interrupt)

	def braille(self, text: str):
		"""
		Brailles the given text.

		:param text: The text to be Brailled
		:type text: str
		"""
		self.output.braille(text)

	def both(self, text: str, interrupt: bool = True):
		"""
		Outputs the given text thrue speech and Braill.

		:param text: The text to output.
		:type text: str
		:param interrupt: Sets if the spoken text should interrupt the currently speaking text, defaults to True
		:type interrupt: bool, optional
		"""
		self.output.speak(text, interrupt = interrupt)
		self.output.braille(text)