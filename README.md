# Bounce-Assignment

## Assumptions:
1. The Scheduler would try to fill rooms first instead of looking for the nearest available time slot
2. Initial config is set in the config.json file
3. In order to keep things simple, the app doesn't remove past dates slots

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install dependencies.
```bash
pip install -r requirements.txt 
```

## Running the app:
```bash
python3 main.py
```

Use the following endpoint the schedule an operation:
```
POST http://0.0.0.0:8000/operating_slot/
```
with json request body:
```
{
    "surgeon_type": "brain"
}
```
supported surgeon types are: brain, heart



