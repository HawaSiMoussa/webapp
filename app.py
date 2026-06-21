from flask import Flask, render_template, request, redirect, url_for, flash
import forms
from db import db, Post, StandardUser
from flask_bootstrap import Bootstrap5

app = Flask(__name__)

app.config.from_mapping(
    SECRET_KEY='secret_key_just_for_dev_environment',
    BOOTSTRAP_BOOTSWATCH_THEME='pulse',
    SQLALCHEMY_DATABASE_URI='sqlite:///lostandfound.sqlite',
    SQLALCHEMY_TRACK_MODIFICATIONS=False
)

db.init_app(app)
bootstrap = Bootstrap5(app)

with app.app_context():
    db.create_all()


# Beim Aufruf der Seite zuerst Login anzeigen
@app.route("/")
def start():
    return redirect(url_for("login"))


# Home-Seite
@app.route("/home/")
def index():
    posts = db.session.execute(
        db.select(Post)
    ).scalars()

    return render_template(
        "home.html",
        posts=posts
    )


# Registrierung
@app.route('/register/', methods=['GET', 'POST'])
def register():

    form = forms.CreateLogin()

    if form.validate_on_submit():

        existing_user = db.session.execute(
            db.select(StandardUser).where(
                StandardUser.hwr_mail == form.hwrmail.data
            )
        ).scalar_one_or_none()

        if existing_user:
            flash("Diese E-Mail wird bereits verwendet!", "warning")
            return redirect(url_for("register"))

        user = StandardUser(
            hwr_mail=form.hwrmail.data,
            passwort=form.passwort.data
        )

        db.session.add(user)
        db.session.commit()

        flash("Account erstellt!", "success")
        return redirect(url_for("login"))

    return render_template(
        "register.html",
        form=form
    )


# Login
@app.route('/login/', methods=['GET', 'POST'])
def login():

    form = forms.CreateLogin()

    if form.validate_on_submit():

        user = db.session.execute(
            db.select(StandardUser).where(
                StandardUser.hwr_mail == form.hwrmail.data
            )
        ).scalar_one_or_none()

        if user is None:
            flash("User existiert nicht.", "warning")
            return redirect(url_for("login"))

        if user.passwort != form.passwort.data:
            flash("Falsches Passwort!", "warning")
            return redirect(url_for("login"))

        return redirect(url_for("index"))

    return render_template("login.html", form=form)

if __name__ == "__main__":
    app.run(debug=True)