#!/usr/bin/python3
"""List of states on HTML states_list"""

from flask import Flask, render_template
from models import storage
from models.state import State
from models.amenity import Amenity
from models.place import Place
from models.user import User

app = Flask(__name__)


@app.route('/hbnb', strict_slashes=False)
def hbnb_filters(id=None):
    """display a HTML page: (inside the tag BODY)"""
    # sort states by name from a to z
    slist = sorted(storage.all(
        State).values(), key=lambda x: x.name)
    for s in slist:
        s.cities.sort(key=lambda x: x.name)

    amenities_list = sorted(storage.all(
        Amenity).values(), key=lambda x: x.name)

    places_list = sorted(storage.all(
        Place).values(), key=lambda x: x.name)

    users_list = storage.all(User)
    for place in places_list:
        for user in users_list.items():
            if f'User.{place.user_id}' == user[0]:
                place.owner = user[1].first_name + " " + user[1].last_name
    return render_template("100-hbnb.html", sorted_states_list=slist,
                           amenities_list=amenities_list,
                           places_list=places_list)


@app.teardown_appcontext
def terminate(exc):
    """close the storage"""
    storage.close()


if __name__ == '__main__':
    """start the server"""
    app.run(host='0.0.0.0', port=5000)
