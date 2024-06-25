"""
enum Factory for electrode.
"""

from enum import Enum

def CreateEnum(name: str, **kwargs):
	"""
	Creates an enum with spesified keys and values.

	:param name: The name of the enum
	:type name: str
	"""
	return Enum(name, kwargs)