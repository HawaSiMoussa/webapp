
import os
from flask_mail import Mail, Message

from flask import Flask, render_template
from flask_bootstrap import Bootstrap5  

app = Flask(__name__)
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.environ.get('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = os.environ.get('MAIL_PASSWORD')


app.config.from_mapping(
    SECRET_KEY = 'secret_key_just_for_dev_environment',
    BOOTSTRAP_BOOTSWATCH_THEME = 'pulse'
)
db.init_app(app)
bootstrap = Bootstrap5(app)
mail = Mail(app)

@app.route("/")
def index():

    posts = [
        {
            "username": "Sarah",
            "title": "Schwarzer Rucksack",
            "views": 12,
            "DateOfLoss": "2024-06-01",
             "LocationOfLoss": " Haus C Raum 1.08",
             "description": "Ein schwarzer Rucksack mit großem Logo.",
             "hwrMail": "sarah@hwr-berlin.de"
        },
        {
            "username": "Max",
            "title": "Laptop",
            "views": 5,
            "DateOfLoss": "2024-04-01",
             "LocationOfLoss": "Cafeteria Haus B",
             "description": "Ein schwarzes Laptop mit großem Logo.",
             "hwrMail": "max@hwr-berlin.de"
        },
        {
            "username": "Laura",
            "title": "Schlüsselbund",
            "views": 8,
            "DateOfLoss": "2024-05-01",
            "LocationOfLoss": "Bibliothek Haus A",
            "description": "Ein schwarzer Rucksack mit großem Logo.",
            "hwrMail": "laura@hwr-berlin.de"
        }
    ]

    return render_template(
        "home.html",
        posts=posts
    )
#links: name der an html übergeben wird, rechts name der variable in python
@app.route('/testmail')
def testmail():

    msg = Message(
        subject="Flask-Mail Test",
        recipients=["useto.test.169@gmail.com"]
    )

    msg.body = "Hallo, diese Mail wurde über Flask-Mail versendet."

    mail.send(msg)

    return "Mail verschickt!"

if __name__ == "__main__":
    app.run(debug=True)