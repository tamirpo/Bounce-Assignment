from dataclasses import dataclass
from typing import List

from dataclasses_json import dataclass_json

from model.room import Room


@dataclass_json
@dataclass(frozen=True, eq=True)
class Config:
	working_hours_start: str
	working_hours_end: str
	max_days_ahead_to_schedule: int
	rooms: List[Room]
