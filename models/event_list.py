from models.event import Event
from datetime import date
from datetime import time

event_1 = Event(
    date(2021, 12, 12),
    time(13, 00, 00),
    "How to Read",
    25,
    25,
    "St. Martin's Church",
    "Do you not know how to read? Well, that's pretty incredible that you can read about this event listing.",
    True,
)
event_2 = Event(
    date(2021, 12, 13),
    time(10, 00),
    "Salsa Pals",
    13,
    20,
    "Park Lane Halls",
    "Learn the art of Salsa dancing with a friend. Bring your own or pick one up at the event.",
    False,
)

events = [event_1, event_2]


def add_event(add_new_event):
    events.append(add_new_event)
