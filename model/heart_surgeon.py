from enums.machine_types import MachineTypes
from enums.operation_types import OperationTypes
from model.doctor import Doctor
from model.room import Room


class HeartSurgeon(Doctor):

	def type(self):
		return OperationTypes.Heart

	def get_surgery_duration(self, room: Room):
		"""Get Duration of surgery (in minutes) based on existing machines in the given room.
		If the required machines do not exist in the room - the surgery cannot be done and the result is -1.
		"""
		result = -1
		for machine in room.machines:
			if machine.type == MachineTypes.ECG.value:
				result = 180
				break
		return result
