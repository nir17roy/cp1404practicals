"""
CP1404/CP5632 Practical
Simple Flask App
"""

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/greet/<name>')
def greet(name):
    return render_template('greet.html', name=name)


if __name__ == '__main__':
    app.run(debug=True)
