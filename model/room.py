from datetime import datetime, timedelta
from typing import List

from model.machine import Machine


class Room:
	TIME_FORMAT = '%H:%M'
	DATE_FORMAT = '%d-%m-%Y'

	def __init__(self, room_id: int, machines: List[Machine], operating_hours_start: str, operating_hours_end: str):
		self.room_id = room_id
		self.operating_hours_start = operating_hours_start
		self.operating_hours_end = operating_hours_end
		self.calendar = self.init_calendar()
		if machines is not None:
			self.machines = machines
		else:
			self.machines = []

	def init_calendar(self) -> dict[str, dict]:
		calendar = {}
		today = datetime.today().strftime(self.DATE_FORMAT)
		start_time = max(self.operating_hours_start, datetime.now().strftime(self.TIME_FORMAT))
		end_time = self.operating_hours_end
		calendar = self.add_day_to_calendar(calendar=calendar, day=today, start_time=start_time, end_time=end_time)

		return calendar

	def add_day_to_calendar(self, calendar, day, start_time, end_time):
		if not start_time:
			start_time = self.operating_hours_start
		if not end_time:
			end_time = self.operating_hours_end
		start_time_formatted = datetime.strptime(start_time, self.TIME_FORMAT)
		end_time_formatted = datetime.strptime(end_time, self.TIME_FORMAT)
		calendar[day] = {}
		current_time = start_time_formatted
		while current_time < end_time_formatted:
			calendar[day][datetime.strftime(current_time, self.TIME_FORMAT)] = False
			current_time = current_time + timedelta(minutes=1)

		return calendar

	def add_machine(self, machine: Machine):
		self.machines.append(machine)

