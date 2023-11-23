"""
Command class for electrode.
"""

class Command:
	"""
	The class that all commands should inherit from.
	"""
	def __init__(self, *args, **kwargs):)		
		self.requires=None
		self.args=args
		self.kwargs=kwargs

	def execute(self): raise NotImplementedError(f'Every command class must have an execute function. The class {self} does not.')

	def isRunning(self): raise NotImplementedError(f'Every command class must have an isRunning function. The class {self} does not.')