#!/usr/bin/python3
"""Flask web application for displaying a list of states.

This application runs on 0.0.0.0 with port 5000.
Routes:
    /states_list: Displays an HTML page with a sorted
    list of State objects from DBStorage.
"""
from models import storage
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/states_list", strict_slashes=False)
def states_list():
    """Renders an HTML page with a sorted list of all State
    objects in DBStorage.
    """
    states = storage.all("State")
    return render_template("7-states_list.html", states=states)


@app.teardown_appcontext
def teardown(exc):
    """Closes the current SQLAlchemy session."""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0")
