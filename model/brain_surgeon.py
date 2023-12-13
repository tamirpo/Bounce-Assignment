from enums.machine_types import MachineTypes
from enums.operation_types import OperationTypes
from model.doctor import Doctor
from model.room import Room


class BrainSurgeon(Doctor):

	def type(self):
		return OperationTypes.Brain

	def get_surgery_duration(self, room: Room):
		"""Get Duration of surgery (in minutes) based on existing machines in the given room.
		If the required machines do not exist in the room - the surgery cannot be done and the result is -1.
		"""
		result = -1
		found_mri_machine = False
		for machine in room.machines:
			if machine.type == MachineTypes.MRI.value:
				found_mri_machine = True
				result = 180
				break
		if found_mri_machine:
			for machine in room.machines:
				if machine.type == MachineTypes.CT.value:
					result = 120
					break

		return result
