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

	def load(self, language):
		if language in self.cache:
			return self.cache[language]

		try:
			with open(f"{self.directory}{language}.json") as f:
				translation_data = json.load(f)
				self.cache[language] = translation_data
				return translation_data
		except FileNotFoundError as e:
			raise FileNotFoundError(f"Error: Translation file '{self.directory}{language}.json' not found.")

	def translate(self, key, language, **kwargs):
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


# Example usage:
translator = Translator()
text = translator.translate("health", "english", health=10)
text2 = translator.translate("tired", "english")
print(text)
print(text2)
