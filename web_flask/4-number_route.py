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


@app.route('/python', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def hello_python(text):
    """Returns a string at the Python route,
    expanded using the text variable and a default text value"""
    newt = text.replace('_', ' ')
    return 'Python %s' % newt


@app.route('/number/<int:n>', strict_slashes=False)
def number_route(n):
    """Returns a string at the Number route,
    expanded using the text variable"""
    if type(n) == int:
        return '%i is a number' % n


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
