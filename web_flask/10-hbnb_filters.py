#!/usr/bin/python3
"""This script starts a Flask web server"""
from flask import Flask, escape, render_template
from models import storage
from models.state import State
from models.amenity import Amenity
app = Flask(__name__)


@app.route('/hbnb_filters', strict_slashes=False)
def states():
    """/hbnb_filters: display a HTML page like 6-index.html,
    AirBnB clone - Web static"""
    states = storage.all('State').values()
    amenities = storage.all('Amenity').values()
    return render_template('10-hbnb_filters.html', states=states, amenities=amenities)


@app.teardown_appcontext
def teardown(self):
    """Removes the current SQLAlchemy
    and closes it"""

    storage.close()


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
