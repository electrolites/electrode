import json

class Translator:
	"""
	Translation class for electrode.
	"""
	def __init__(self, translationDirectory: str = ""):
		"""
		Initialize the translater.

		:param translationDirectory: The directory in wich the translation files are found., defaults to ""
		:type translationDirectory: str, optional
		"""
		self.directory = translationDirectory
		self.cache = {}

	def load(self, language: str):
		"""
		Gets the spesifide language, loading it from a file if it has not yet been cached.

		:param language: The language to be loaded.
		:type language: str
		:raises FileNotFoundError: If the languages json file is not found in the language directory.
		:return: The data for the language
		:rtype: dict
		"""
		if language in self.cache:
			return self.cache[language]

		try:
			with open(f"{self.directory}{language}.json") as f:
				translation_data = json.load(f)
				self.cache[language] = translation_data
				return translation_data
		except FileNotFoundError as e:
			raise FileNotFoundError(f"Error: Translation file '{self.directory}{language}.json' not found.")

	def translate(self, key: str, language: str, **kwargs):
		"""
		Translates a frase to a spesifide language.

		:param key: The word or fraze to be translated.
		:type key: str
		:param language: The language to translate to.
		:type language: str
		:raises KeyError: When the language does not have a place holder value for the formating of the fraze.
		:raises IndexError: When there is to many place holders in the provided fraze.
		:return: The translateed frase
		:rtype: str
		"""
		translation_data = self.load(language)
		translatedPhrase = translation_data.get(
			key, f"{key} not available in {language}")

		try:
			translatedPhrase = translatedPhrase.format(**kwargs)
			return translatedPhrase
		except KeyError as e:
			raise KeyError(f"Error: Missing placeholder value for {e} in the translation of '{key}' ({language}).")
		except IndexError as e:
			raise IndexError(f"Error: Index out of range in the translation of '{key}' ({language}). Check placeholder count.")

"""
Example usage:
translator = Translator()
text = translator.translate("health", "english", health=10)
text2 = translator.translate("tired", "english")
print(text)
print(text2)
"""