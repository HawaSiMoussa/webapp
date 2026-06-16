import os

from flask import Flask, render_template
from requests import 
from flask_bootstrap import Bootstrap5  # (1.)

app = Flask(__name__)

bootstrap = Bootstrap5(app)

@app.route("/")
def index():
    return render_template("home.html")

if __name__ == "__main__":
    app.run(debug=True)