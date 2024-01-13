#!/usr/bin/python3
"""start a flack server listening on port 5000 handling '/'"""
from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """handling / route"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """handling hbnb route"""
    return "HBNB"


if __name__ == '__main__':
    """start the server"""
    app.run(host='0.0.0.0', port=5000)
