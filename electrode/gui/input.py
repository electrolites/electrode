"""
Virtual input class for electrode.
"""
import re
import string
from electrode.gui.keyboard import Keyboard
from electrode.core.speech import Speech

class Input:
	def __init__(self, initialText="", password=True, passwordChar="*", enter=True, escape=True, repeatChars=False, repeatWords=True, maxLength=0, keyDelay=500, keyRepeat=80, keyboard=Keyboard(), speech = Speech(0)):
		self.string=initialText
		self.cursor=len(self.string)
		self.selection=self.string
		self.startSelection=0
		self.endSelection=0
		self.lines=re.split("\r?\n", self.string)
		self.currentline=0
		self.password=password
		self.passwordChar=passwordChar
		self.enter=enter
		self.escape=escape
		self.keyDelay=keyDelay
		self.keyRepeat=keyRepeat
		self.repeatChars=repeatChars
		self.repeatWords=repeatWords
		self.maxLength=maxLength
		self.keyboard=keyboard
		self.speech=speech
		self.allowedCharacters = list(string.printable)

	def toggleRepeatChars(self):
		self.repeatChars=True if self.repeatChars=False else False
		return self.repeatChars

	def toggleRepeatWords(self):
		self.repeatWords=True if self.repeatWords=False else False
		return self.repeatWords

	def move(self, value: int):
		tempCursor=self.cursor+value
		if tempCursor<0: tempCursor=0
		elif tempCursor >len(self.string): tempCursor=len(self.string)
		self.cursor=tempCursor
		self.selection=self.getChar()
		self.startSelection=self.cursor
		self.endSelection=self.cursor

	@property
	def isAtMaxLength(self):
		if self.maxLength=-1: return False
		return len(self.string)>=self.maxLength

	@property
	def text(self):
		return self.string

	@text.setter
	def text(self, text):
		self.string=text
		self.cursor=0
		self.selection=self.string
		self.startSelection=0
		self.endSelection=len(self.string)

	def clear(self):
		self.text=""
		self.cursor=0
		self.selection=""
		self.startSelection=0
		self.endSelection=0

	def getChar(self, index=self.cursor):
		if len(self.text)<=0: return ""
		return self.string[index]

	def addChar(self, character):
		if len(character)==0: return
		if self.cursor<len(self.string): self.string= self.string[:self.cursor]+character+self.string[self.cursor:]
		else: self.string+=character
		self.cursor+=len(character)
		self.startSelection=self.cursor
		self.endSelection=self.cursor
		if re.match("\r?\n",character):
			self.lines=re.split("\r?\n", self.string)

	def removeChar(self):
		if self.cursor==0: return
		character=self.string[self.cursor-1]
		if re.match("\r?\n",character):
			self.lines=re.split("\r?\n", self.string)
		if self.cursor==len(self.string): self.string=self.string[:-1]
		else: self.string=self.string[:self.cursor-1] + self.string[:self.cursor]
		self.cursor-=1
		self.selection=self.getChar()
		self.startSelection=self.cursor
		self.endSelection=self.cursor

	def speakChar(self, character: str):
		spoken=character
		if spoken==" ": spoken="space"
		if spoken.isupper(): spoken+=f'cap {spoken}'
		if spoken=="\n" or spoken=="\r": spoken="new line"
		if self.password==True: self.spoken=self.passwordChar
		self.speech.speak(spoken)

	def speakSelection(self):
		spoken=""
		if len(self.selection)>1000 or self.password:
			spoken=f'{len(self.selection)}characters selected'
			if len(self.selection)!=len(self.text): spoken+=f' from {len(self.text)}'
		else:
			spoken=f'{self.selection} selected'

	def topSnap(self):
		self.cursor=0
		self.selection=self.getChar()
		self.cursor=0
		self.startSelection=self.cursor
		self.endSelection=self.cursor
		self.speakChar(self.getChar())

	def bottomSnap(self):
		self.cursor=len(self.string)
		self.startSelection=self.cursor
		self.endSelection=self.cursorself.selection=self.getChar()
		self.cursor=0
		self.speakChar(self.getChar())

	def topSelect(self):
		self.selection=self.text[0:self.cursor]
		self.startSelection=0
		self.endSelection=self.cursor
		self.cursor=0
		self.speakSelection()

	def bottomSelect(self)
		self.selection=self.text[self.cursor:]
		self.startSelection=self.cursor
		self.endSelection=len(self.string)
		self.cursor=len(self.text)

	def inputLetters(self):
		self.allowedCharacters=list(string.ascii_letters)

	def inputDigits(self, allowNegative=True, allowDecimal=False):
		self.allowedCharacters=list(string.digits)
		if allowNegative: self.allowedCharacters.append("-")
		if allowDecimal: self.allowedCharacters.append(".")

	def inputAll(self):
		self.allowedCharacters=list(string.printable)

	def inputCustom(self, *chars):
		self.allowedCharacters=list(*chars)

	def _getWord(self, direction: int):
		wordString=re.sub("\r?\n", " 1nl2 ", self.text)
		tempCursor=0
		if direction<=0:
			if self.cursor!=0: index=wordString.rfind(" ", 0, self.cursor-1)
			else: index=0
			if Index<0:
				Index=len(self.string)
				tempCursor-=self.cursor
			else: 
				tempCursor=index - self.cursor
			endIndex=wordString.find(" ", tempCursor + 1)
			if endIndex<0: endIndex=len(self.string)
			word=wordString[index:endIndex]
			return word, tempCursor, index
		if direction>=1:
			if tempCursor!=self.cursor: index=wordString.find(" ", self.cursor+1)
			else: index=len(wordString)
			if index<0: index=len(wordString)
			tempCursor+=index - self._cursor
			startIndex = wordString.rfind(" ", 0, tempCursor - 1)
			if startIndex<0: startIndex=0
			word=wordString[startIndex:index]
			return word, tempCursor, index

	def _getSpokenWord(self, word: str):
		if word.strip()=="1nl2":
			return "new line"
		if self.password:
			spoken=""
			spoken+=self.passwordChar*len(word)
			return spoken
		return word

	def moveWord(self, direction: int)
		word, self.cursor, _, __=self._getWord(direction)
		self.speech.speak(self._getSpokenWord(word))

	def selectWord(self, direction: int):
		spokenEdition=""
		word=""
		if direction<=0:
			word, self.cursor, index=self._getWord(direction)
			if index<self.startSelection:
				spokenEdition=="selected"
				self.startSelection=index
			elif index>self.startSelection:
				spokenEdition="unselected"
				self.endSelection=index+1
		elif direction>0:
			word, self.cursor, index=self._getWord(direction)
			if index>=self.endSelection:
				spokenEdition="selected"
				self.endSelection=index
			elif index<self.endSelection:
				spokenEdition="unselected"
				self.startSelection=index
		self.selection=self.text[self.startSelection:self.endSelection]
		self.speech.speak(f'{self._getSpokenWord(word)} {spokenEdition}')

	def moveWordLeft(self): self.moveWord(-1)

	def moveWordRight(self): self.moveWord(1)

	def selectWordLeft(): self.selectWord(-1)

	def selectWordRight(): self.selectWord(1)

	def _processDeleteEvent(self, control: bool):
		if self.cursor==0: return
		if self.string=="":
			self.speech.speak("blank")
			return
		if control:
			word, tempCursor, index=self._getWord(-1)
			endIndex=index+len(word)
			self.speech.speak(f'{word} deleted')
			self.string=self.string[:index]+self.string[endIndex+1:]
			self.cursor=tempCursor-1
			self.startSelection=self.cursor
			self.endSelection=self.cursor
			self.selection=self.getChar()
		if self.startSelection==self.endSelection:
			character=self.getChar(self.cursor-1)
			self.removeChar()
			self.speakChar(f'{character} deleted')
			return
		if self.endSelection<1000:
			self.speech.speak(f'{self.selection} deleted')
		else:
			self.speech.speak(f'deleted from {self.startSelection} to {self.endSelection}')
		if self.startSelection==0 and self.endSelection==len(self.string):
			self.clear()
			return
		if self.startSelection==0:
			self.string=self.string[self.endSelection+1:]
			self.cursor=0
			self.startSelection=self.cursor
			self.endSelection=self.cursor
			self.selection=self.getChar()
			return
		self.cursor=self.startSelection-1
		self.string=self.string[:self.startSelection-1]+self.string[self.endSelection+1:]
		self.startSelection=self.cursor
		self.endSelection=self.cursor
		self.selection=self.getChar()

	def moveLine(self, direction):
		self.currentline+=direction
		self.speech.speak(self.lines[self.currentline])
		self.cursor=len(self.string)-len(self.lines[self.currentline])

	def _handleAeroEvent(self, direction: int, shift: bool, control: bool):
		if direction<0:
			if not shift and not control:
				self.move(-1)
				self.speakChar(self.getChar())
				return
			if control and not shift:
				self.moveWordLeft()
				return
			if shift and not control:
				self.startSelection-=1 if self.startSelection >0 else 0
				self.speech.speak(f'{self.getChar(self.startSelection)} selected')



	def push(self, handler):
		if self.keyboard.keyPressed(self.keyboard.keyConstants.key_enter) :
			if self.enter and self.keyboard.keyUp(self.keyboard.keyConstants.key_shift): handler(self.text)
			elif self.keyboard.keyDown(self.keyboard.keyConstants.key_shift): self.addChar("\r\n")
		elif self.keyboard.keyPressed(self.keyboard.keyConstants.key_escape) and self.escape: self.handler("")
		elif self.keyboard.keyPressed(self.keyboard.keyConstants.key_backspace):
			self._processDeleteEvent(self.keyboard.keyDown(self.keyboard.keyConstants.key_control))
			self.lines=re.split("\r?\n", self.string)
		if self.keyboard.keyPressed(self.keyboard.keyConstants.key_down): self.moveLine(-1)
		if self.keyboard.keyPressed(self.keyboard.keyConstants.key_up): self.moveLine(-1)
