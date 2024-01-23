import os
import zipfile


class Pack:
	def __init__(self, file: str, key: str = ""):
		self.path=file
		if os.path.isfile(file):
			self.data=self._unpack(key)
		else: raise ValueError(f'file must be a directory the path {self.path} does not exist as a file.')

	def _unpack(self, key: str = ""):
		zf = zipfile.ZipFile(self.path)
		if key=="":
			return {name: zf.open(name) for name in zf.namelist()}
		return {name: zf.open(name, pwd = key.encode('utf-8')) for name in zf.namelist()}