# -*- coding: utf-8 -*-

from flask import Flask, request, url_for, render_template

# create Flask app
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.debug = True
    app.run()