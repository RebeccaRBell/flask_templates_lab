from datetime import date
from datetime import time


class Event:
    def __init__(
        self,
        date,
        time,
        event_name,
        number_of_guests,
        capacity,
        room_location,
        description,
        recurring,
    ):
        self.date = date
        self.time = time
        self.event_name = event_name
        self.number_of_guests = number_of_guests
        self.capacity = capacity
        self.room_location = room_location
        self.description = description
        self.recurring = recurring
