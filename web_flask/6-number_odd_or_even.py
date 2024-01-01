#!/usr/bin/python3
"""This script starts a Flask web application"""

from flask import Flask
from flask import render_template
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


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """Returns a HTML page if n is an integer"""
    if type(n) == int:
        return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_odd_or_even(n):
    """Returns a template at the /number_odd_or_even/<n>
    route, display if the number is odd or even"""
    if type(n) == int:
        return render_template('6-number_odd_or_even.html', n=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
