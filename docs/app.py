
import os

from flask import Flask, render_template
from flask_bootstrap import Bootstrap5  

app = Flask(__name__)

bootstrap = Bootstrap5(app)
app.config.from_mapping(
    SECRET_KEY = 'secret_key_just_for_dev_environment'),
    BOOTSTRAP_BOOTSWATCH_THEME = 'pulse'
bootstrap = Bootstrap5(app)

@app.route("/")
def index():

    posts = [
        {
            "username": "Sarah",
            "title": "Schwarzer Rucksack",
            "views": 12,
            "DateOfLoss": "2024-06-01",
             "LocationOfLoss": " Haus C Raum 1.08",
             "description": "Ein schwarzer Rucksack mit großem Logo."
        },
        {
            "username": "Max",
            "title": "Laptop",
            "views": 5,
            "DateOfLoss": "2024-04-01",
             "LocationOfLoss": "Cafeteria Haus B",
             "description": "Ein schwarzes Laptop mit großem Logo."
        },
        {
            "username": "Laura",
            "title": "Schlüsselbund",
            "views": 8,
            "DateOfLoss": "2024-05-01",
            "LocationOfLoss": "Bibliothek Haus A",
            "description": "Ein schwarzer Rucksack mit großem Logo."
        }
    ]

    return render_template(
        "home.html",
        posts=posts
    )
#links: name der an html übergeben wird, rechts name der variable in python

if __name__ == "__main__":
    app.run(debug=True)