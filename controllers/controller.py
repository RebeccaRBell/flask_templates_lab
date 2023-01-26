from flask import render_template, request  # ADDED
from app import app
from models.event import Event
from models.event_list import events, add_event


@app.route("/")
def index():
    return render_template("index.html", events=events)


@app.route("/", methods=["POST"])
def input_event():
    new_event_date = request.form["date"]
    new_event_time = request.form["time"]
    new_event_name = request.form["name"]
    new_event_guests = 0
    new_event_capacity = request.form["capacity"]
    new_event_location = request.form["location"]
    new_event_description = request.form["description"]
    recurring = bool
    add_new_event = Event(
        new_event_date,
        new_event_time,
        new_event_name,
        new_event_guests,
        new_event_capacity,
        new_event_location,
        new_event_description,
        recurring,
    )
    add_event(add_new_event)

    return render_template("index.html", events=events)
