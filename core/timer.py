"""
Timer for electrode.
"""
import time

class Timer:
	def __init__(self, resetThreshold=0):
		self.initTime=time.time()
		self.pausedTime=self.initTime
		self.paused=False
		self.resetThreshold=resetThreshold

	@property
	def time(self):
		if self.paused: return self.pausedTime
		currentTime=self._timeMs(self.initTime-time.time())
		if currentTime>=self.resetThreshold and self.resetThreshold>0:
			self.restart()
			currentTime=self._timeMs(self.initTime-time.time())
		return currentTime

	@time.setter
	def time(self, t: int):
		self.initTime=time.Time(-t/1000)
		self.pausedTime=self.initTime

	def restart(self):
		self.__init__()

	def pause(self):
		self.paused=True
		self.pausedTime=self.time

	def resume(self):
		if self.paused==False: return
		self.paused=False
		self.time=self._timeMs(self.pausedTime)

	def _timeMs(self, t):
		return int(round(t*1000))