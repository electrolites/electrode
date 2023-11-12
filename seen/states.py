"""
States that any given seen can be in.
"""
from enum import Enum

class States(Enum):
	INITIAL=1000
	PUSHED=1001
	ENTERD=1002
	EXITED=1003
	POPPED=1004