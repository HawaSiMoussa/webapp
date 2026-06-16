import os

from flask import Flask, render_template, redirect, url_for
from requests import post
from flask_bootstrap import Bootstrap5  # (1.)
import db, forms

app = Flask(__name__)

bootstrap = Bootstrap5(app)

@app.route("/")
def index():
    return render_template("home.html")

if __name__ == "__main__":
    app.run(debug=True)