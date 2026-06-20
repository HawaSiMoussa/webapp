from flask import Flask, render_template
from flask_bootstrap import Bootstrap5



app = Flask(__name__)

app.config.from_mapping(
    SECRET_KEY='secret_key_just_for_dev_environment',
    BOOTSTRAP_BOOTSWATCH_THEME='pulse',
    SQLALCHEMY_DATABASE_URI='sqlite:///lostandfound.sqlite',
    SQLALCHEMY_TRACK_MODIFICATIONS=False
)
from instance.db import db, Post

bootstrap = Bootstrap5(app)

db.init_app(app)

with app.app_context():
    db.create_all()


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