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


@app.route('/states/<id>', strict_slashes=False)
def states(state_id=None):
    """display the states and cities listed in alphabetical order"""
    states_o = storage.all("State")
    if state_id is not None:
        state_id = 'State.' + state_id
    return render_template('9-states.html', states_o=states_o,
                           state_id=state_id)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
