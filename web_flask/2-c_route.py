#!/usr/bin/python3
"""This script starts a Flask web application"""

from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_flask():
    """Returns a string at the root route"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Returns a string at the hbnb route"""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def cisfun(text):
    """Returns a string at the C route,
    expanded using the text variable"""
    newt = text.replace('_', ' ')
    return 'C %s' % newt


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
