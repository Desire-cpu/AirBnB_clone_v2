#!/usr/bin/python3
"""This script starts a Flask web server"""
from flask import Flask, render_template
from models import storage
from models.state import State
app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def states_list():
    """Returns a rendered html template at the /states_list route"""

    return render_template('7-states_list.html',
                           states=storage.all('State').values())


@app.teardown_appcontext
def teardown(self):
    """Removes the current SQLAlchemy"""

    storage.close()


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
