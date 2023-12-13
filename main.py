import uvicorn

from enums.operation_types import OperationTypes
from model.brain_surgeon import BrainSurgeon
from model.heart_surgeon import HeartSurgeon
from model.hospital import Hospital
from model.machine import Machine
from or_scheduler import ORScheduler

import os

from fastapi import FastAPI, Request
from config import Config

CONFIG_FILE_PATH = os.environ.get('CONFIG', 'config.json')
CONFIG = Config.from_json(open(CONFIG_FILE_PATH, "r").read())

app = FastAPI()


@app.post("/operating_slot/")
async def set_operating_slot(request: Request):
    doctor = HeartSurgeon()
    request_body = await request.json()

    if request_body['surgeon_type'] == OperationTypes.Brain.value:
        doctor = BrainSurgeon()
    response = app.scheduler.schedule_operation(doctor=doctor)
    return response


if __name__ == '__main__':

    operating_hours_start = CONFIG.working_hours_start
    operating_hours_end = CONFIG.working_hours_end
    max_days_ahead_to_schedule = CONFIG.max_days_ahead_to_schedule

    hospital = Hospital()
    for room in CONFIG.rooms:
        machines = []
        for machine in room["machines"]:
            machines.append(Machine(machine['type']))
        hospital.add_room(machines=machines,
                          operating_hours_start=operating_hours_start,
                          operating_hours_end=operating_hours_end)

    app.scheduler = ORScheduler(hospital, max_days_ahead_to_schedule=max_days_ahead_to_schedule)
    uvicorn.run(app, host="0.0.0.0", port=8000)
