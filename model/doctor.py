from abc import ABC, abstractmethod
from model.room import Room


class Doctor(ABC):

	@property
	def type(self):
		pass

	@abstractmethod
	def get_surgery_duration(self, room: Room):
		"""Get Duration of surgery (in minutes) based on existing machines in the given room.
		If the required machines do not exist in the room - the surgery cannot be done and the result is -1.
		"""
		pass
