"""
Contains all the factories and factory makers  for electrodes internals.
"""

from typing import Callable

from audio.manager import Manager as AudioManager
from core.speech import Speech as CoreSpeech
from core.timer import Timer as CoreTimer
from core.translator import Translator as CoreTranslator
from gui .window import Window as GuiWindow
from mapping.map import Map as MappingMap

def makeMap(minX: int, maxX: int, minY: int, maxY: int, minZ: int, maxZ: int, dynamic: bool):
	return MappingMap(minX= minX, maxX = maxX, minY = minY, maxY = maxY, minZ = minZ, maxZ =maxZ, dynamic= dynamic)

def mapFactory(minX: int, maxX: int, minY: int, maxY: int, minZ: int, maxZ: int, dynamic: bool):
	def factory():
		return makeMap(minX= minX, maxX = maxX, minY = minY, maxY = maxY, minZ = minZ, maxZ =maxZ, dynamic= dynamic)
	return factory

def makeTranslator(path: str):
	return CoreTranslator(path)

def translaterFactory(path: str):
	def factory():
		return makeTranslator(path)
	return factory

def makeTimer(resetThreshold: int):
	return CoreTimer(resetThreshold = resetThreshold)

def timerFactory(resetThreshold: int):
	def factory():
		return makeTimer(resetThreshold)
	return factory

def audioManagerFactory(eventManager):
	def factory(path: str, key: str = ""):
		return AudioManager(path, eventManager, key =key)
	return factory