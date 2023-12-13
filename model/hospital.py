from typing import List

from enums.operation_types import OperationTypes
from model.machine import Machine
from model.room import Room


class Hospital:

	def __init__(self):
		self.rooms = []
		self.operations_queues = {
			OperationTypes.Brain: [],
			OperationTypes.Heart: []
		}

	def add_room(self, machines: List[Machine], operating_hours_start: str, operating_hours_end: str):
		new_room = Room(room_id=len(self.rooms), machines=machines,
						operating_hours_start=operating_hours_start, operating_hours_end=operating_hours_end)
		self.rooms.append(new_room)
