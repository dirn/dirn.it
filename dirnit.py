#!/usr/bin/env python

from flask import Flask, redirect

app = Flask(__name__)


@app.route('/<string:hash>')
def send_redirect(hash):
    return redirect('http://dirn.it/' + hash, code=301)
