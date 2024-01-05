#!/usr/bin/python3
"""Flask web application to display a list of
states and their related cities.

This application runs on 0.0.0.0 with port 5000.
Routes:
    /cities_by_states: Renders an HTML page with a sorted
    list of all states and their related cities.
"""
from models import storage
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/cities_by_states", strict_slashes=False)
def cities_by_states():
    """Renders an HTML page with a sorted list of
    all states and their related cities.

    States and cities are sorted by name.
    """
    states = storage.all("State")
    return render_template("8-cities_by_states.html", states=states)

@app.teardown_appcontext
def teardown(exc):
    """Closes the current SQLAlchemy session."""
    storage.close()

if __name__ == "__main__":
    app.run(host="0.0.0.0")
