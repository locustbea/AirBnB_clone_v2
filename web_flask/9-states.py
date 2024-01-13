#!/usr/bin/python3
"""List of states on HTML states_list"""

from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.route('/states/<id>', strict_slashes=False)
@app.route('/states', strict_slashes=False)
def states_and_state(id=None):
    """display a HTML page: (inside the tag BODY)"""
    # sort states by name from a to z
    slist = sorted(storage.all(
        State).values(), key=lambda x: x.name)
    if id is None:
        return render_template("9-states.html", sorted_states_list=slist,
                               states=True)
    else:
        # sort cities by name from a to z
        for s in slist:
            if s.id == id:
                s.cities.sort(key=lambda x: x.name)
                return render_template("9-states.html", state=s)
    return render_template("9-states.html")


@app.teardown_appcontext
def terminate(exc):
    """close the storage"""
    storage.close()


if __name__ == '__main__':
    """start the server"""
    app.run(host='0.0.0.0', port=5000)
