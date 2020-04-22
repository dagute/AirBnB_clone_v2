#!/usr/bin/python3
"""starts a Flask web application"""
from flask import Flask, render_template
from models import *
from models import storage
app = Flask(__name__)


@app.teardown_appcontext
def tear_down(self):
    """closes the storage"""
    storage.close()


@app.route('/states', strict_slashes=False)
def display_states():
    """Display all states objects"""
    state = storage.all('State')
    return render_template('9-states.html', state=state)


@app.route('/states/<id>', strict_slashes=False)
def states(id):
    """display html page"""
    state = storage.all("State")
    return render_template('9-states.html', state=state, id=id)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
