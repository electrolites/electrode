"""
Convert pygame key locals to be used with electrode.
"""
from pygame import locals

class KeyConstantsMeta(type):
	def __getattr__(self, name: str):
		keyName=name.lower().replace("key_","")
		try:
			return getattr(locals,f'K_{keyName}')
		except AttributeError:
			pass
		try:
			return getattr(locals,f'K_{keyName.upper()}')
		except AttributeError:
			pass
		raise AttributeError(f'The key "{name}" is not a valid keyboard key. Use a format like "key_A" or "KEY_A".')

	def __dir__(self):
		keys=[f'key_{d.lower().replace("k_", "")}' for d in dir(locals) if d.startswith("K_")]
		return keys

class KeyConstants(metaclass=KeyConstantsMeta):
	"""
	Represents the KeyConstants for electrode
	"""