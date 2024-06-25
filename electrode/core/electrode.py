"""
Contains the main functions and loop for electrode.
"""
import asyncio

from audio.manager import Manager as AudioManager
from events.manager import Manager as EventManager
from gui .window import Window as GuiWindow
from mapping.map import Map as MappingMap
from scene.manager import Manager as SceneManager
from core.enumbs import CreateEnum as CoreCreateEnum
from core.speech import Speech as CoreSpeech
from core.timer import Timer as CoreTimer
from core.translator import Translator as CoreTranslator

class Electrode:
	def __init__(self):
		"""
		initializes the main electrode class.
		"""
		self.eventManager = EventManager()
		self.AsyncLoop = asyncio.get_event_loop()
		self.AsyncLoop

