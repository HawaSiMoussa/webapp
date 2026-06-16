
from flask import Flask, render_template
from flask_bootstrap import Bootstrap5  

app = Flask(__name__)

bootstrap = Bootstrap5(app)

@app.route("/")
def index():

    posts = [
        {
            "username": "Sarah",
            "title": "Schwarzer Rucksack",
            "views": 12,
            "DateOfLoss": "2024-06-01",
        },
        {
            "username": "Max",
            "title": "Laptop",
            "views": 5,
            "DateOfLoss": "2024-04-01",
        },
        {
            "username": "Laura",
            "title": "Schlüsselbund",
            "views": 8,
            "DateOfLoss": "2024-05-01",
        }
    ]

    return render_template(
        "home.html",
        posts=posts
    )

if __name__ == "__main__":
    app.run(debug=True)