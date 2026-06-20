from flask import Flask, render_template
from flask_bootstrap import Bootstrap5



app = Flask(__name__)

app.config.from_mapping(
    SECRET_KEY='secret_key_just_for_dev_environment',
    BOOTSTRAP_BOOTSWATCH_THEME='pulse',
    SQLALCHEMY_DATABASE_URI='sqlite:///lostandfound.sqlite',
    SQLALCHEMY_TRACK_MODIFICATIONS=False
)


from db import db, Post, StandardUser

db.init_app(app)
bootstrap = Bootstrap5(app)

with app.app_context():
    db.create_all()

    if StandardUser.query.count() == 0:

        user = StandardUser(
            benutzername="Sarah",
            passwort="test",
            hwr_mail="sarah@hwr-berlin.de"
        )

        db.session.add(user)
        db.session.commit()

    user = StandardUser.query.first()

    if Post.query.count() == 0:

        post = Post(
            titel="Schwarzer Rucksack",
            beschreibung="Großer schwarzer Rucksack",
            verlustort="Haus C",
            views=0,
            user_id=user.user_id
        )

        db.session.add(post)
        db.session.commit()


@app.route("/")
def index():

    # Read all posts from database and pass them to home.html template
    posts = db.session.execute(
        db.select(Post)
    ).scalars()

    return render_template(
        "home.html",
        posts=posts
    )


if __name__ == "__main__":
    app.run(debug=True)