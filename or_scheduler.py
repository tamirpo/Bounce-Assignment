import threading
from datetime import datetime, timedelta

from model.doctor import Doctor
from model.hospital import Hospital


class ORScheduler:
	DATE_FORMAT = '%d-%m-%Y'

	def __init__(self, hospital: Hospital, max_days_ahead_to_schedule: int):
		self.hospital = hospital
		self.max_days_ahead_to_schedule = max_days_ahead_to_schedule

	def schedule_operation(self, doctor: Doctor) -> dict:
		result = {}
		try:
			lock = threading.Lock()

			scheduled = False
			scheduled_day = -1
			scheduled_minutes = []
			scheduled_room = None

			with lock:
				for room in self.hospital.rooms:
					if scheduled:
						break
					# Check if room is suitable for the surgery
					duration = doctor.get_surgery_duration(room)
					if duration != -1:
						# Check if there is an available slot for the surgery in the room
						start_date = datetime.today()
						end_date = start_date + timedelta(days=self.max_days_ahead_to_schedule)
						current_date = start_date
						while current_date < end_date:
							if scheduled:
								break
							available_minutes_count = 0
							start_hour = -1
							scheduled_minutes = []
							current_date_formatted = current_date.strftime(self.DATE_FORMAT)
							if current_date_formatted not in room.calendar:
								room.add_day_to_calendar(room.calendar, current_date_formatted, None, None)

							for time_slot in room.calendar[current_date_formatted]:
								if not room.calendar[current_date_formatted][time_slot]:
									if start_hour == -1:
										start_hour = time_slot
									available_minutes_count += 1
									scheduled_minutes.append(time_slot)
									if available_minutes_count == duration:
										scheduled_room = room
										scheduled_day = current_date_formatted
										scheduled = True
										break
								else:
									start_hour = -1
									available_minutes_count = 0
									scheduled_minutes = []

							current_date = current_date + timedelta(days=1)

				if scheduled:
					for hour in scheduled_minutes:
						scheduled_room.calendar[scheduled_day][hour] = True

					result['room_id'] = scheduled_room.room_id
					result['date'] = scheduled_day
					result['start_time'] = scheduled_minutes[0]
					result['end_time'] = scheduled_minutes[-1]
				else:
					self.hospital.operations_queues[doctor.type()].append(doctor)
					result['queue_position'] = len(self.hospital.operations_queues[doctor.type()])
		except Exception as err:
			print(err)
			result = err

		return result

