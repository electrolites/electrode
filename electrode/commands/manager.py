"""
Command Manager class for electrode.
"""
from command import Command
from cmd.sounds import directSound, Sound, groupSound, SoundGroup, OneShotSound
from cmd.seens import newSeen, runNewSeen, exitSeen, popSeen
from commands.requirements import Requirements
from audio.manager import Manager as SoundManager
from mapping.map import Map
from seen.manager import Manager as SeenManager

class Manager:
	def __init__(self, soundManager: SoundManager, map: Map, seenManager: SeenManager):
		self.commands: list[Command]=[]
		self.validCommands={}
		for commandClass in Command.__subclasses__():
			name=commandClass.__name__.replace("Command", "").lower()
		self.validCommands[name]=commandClass
		self.soundManager=soundManager
		self.map=map
		self.seenManager=seenManager

	def push(self):
		for c in self.commands:
			if c.isRunning()==True: continue
			c.execute()
			if c.runOnce==True: self.commands.remove(c)

	def newCommand(self, commandName: str, *args, **kwargs):
		command=None
		if commandName in self.validCommands: command=self.validCommands[commandName]
		else: raise ValueError(f'Command {commandName} not found.')
		param=self.__getRequirement__(command)
		if param is not None: command=command(param, *args, **kwargs)
		else: command=command(*args, **kwargs)
		if not hasattr(command,"execute"): raise RuntimeError(f'The command {command} does not have an execute atribute.')
		elif not callable(command.execute): raise AttributeError(f'The execute atribute of the command {command} is not callable.')
		if not hasattr(command,"runOnce"): raise RuntimeError(f'The object {command} does not have a runOnce atribute.')
		elif not isinstance(command.runOnce,bool): raise AttributeError(f'The runOnce atribute of the command {command} is not a boolian.')
		if not hasattr(command,"isRunning"): raise RuntimeError(f'Commands must have an isRunning function . The {command} command does not have this function.')
		elif not callable(command.isRunning): raise RuntimeError(f'The isRunning atribute of the {command} is not a function.')
		self.commands.append(command)
		return command

	def removeCommand(self, command: Command|int):
		"""
		command can be the instance of command you want to remove, or the index of the command you want to remove.
		"""
		cmd=None
		if isinstance(command, int):
			if not len(self.commands)>=command: raise IndexError(f'The value {command} is not in range of the commands list.')
			cmd=self.commands.pop(command)
		elif command in self.commands:
			cmd=command
			self.commands.remove(command)
		else: raise ValueError(f'Command not found: {command}')
		if hasattr(cmd,"destroy"): cmd.destroy()

	def __getRequirement__(self, command: Command):
		match command.requires:
			case Requirements.map: return self.map
			case Requirements.soundManager: return self.soundManager
			case Requirements.seenManager: param=self.seenManager
			case None: return None