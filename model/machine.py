from enums.machine_types import MachineTypes


class Machine:

	def __init__(self, machine_type: MachineTypes):
		self.type = machine_type
