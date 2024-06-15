"""
Defines the errors related to events.
"""

from typing import Protocol


class eventExistsError(Exception):
	"""
	Error that is razed when an event is allready registered.
	"""
	def __init__(self, eventName: str, currentData: Protocol, TryedData: Protocol):
		"""
		initializes the eventExistsError.

		:param eventName: The name of the event the error occurred on.
		:type eventName: str
		:param currentData: The protocol the event is currently registered with.
		:type currentData: Protocol
		:param TryedData: The data that the event was trying to be registered with.
		:type TryedData: Protocol
		"""
		self.eventName=eventName
		self.currentData=currentData
		self.TryedData=TryedData
		self.message=f'The event {self.eventName} is allready registered with the data {self.currentData} and can not be registered again with the data {self.TryedData}'
		super().__init__(self.message)

class eventMissingError(Exception):
	"""
	Error that is razed when an event is not found in the registered events.
	"""
	def __init__(self, message: str, event: str):
		"""
		Initialize the eventMissingError.

		:param message: The message for the exception.
		:type message: str
		:param event: The name of the event that is missing.
		:type event: str
		"""
		self.event = event
		self.message=message
		super().__init__(self.message)

class invalidEventError(Exception):
	"""
	Error that is razed when an event does not match certain criteria.
	"""
	def __init__(self, message: str, event: str) -> None:
		"""
		Initialize the invalidEventError.

		:param message: The message for the exception.
		:type message: str
		:param event: The name of the event that is invallid.
		:type event: str
		"""
		self.event = event
		self.message = message
		super().__init__(self.message)

class invalidRequirementsError(Exception):
	"""
	Error that is razed when provided requirements go out side an events registration.
	"""
	def __init__(self, message: str, requirements: dict):
		"""
		initialize the invalid requirements error.

		:param message: The message for the exception.
		:type message: str
		:param requirements: The requirements that failed to pass the check.
		:type requirements: dict
		"""
		self.message = message
		self.requirements = requirements
		super().__init__(self.message)