#!/usr/bin/python3
"""start a flack server listening on port 5000 handling '/'"""
from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_route():
    """handling root function"""
    return "Hello HBNB!"


if __name__ == '__main__':
    """start the server"""
    app.run(host='0.0.0.0', port=5000)
