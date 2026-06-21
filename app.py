from flask import Flask, render_template, redirect, url_for, flash, session
import forms
from db import db, Post, StandardUser
from flask_bootstrap import Bootstrap5
from flask import request 


app = Flask(__name__)

app.config.from_mapping(
    SECRET_KEY='secret_key_just_for_dev_environment',
    #BOOTSTRAP_BOOTSWATCH_THEME='pulse',
    SQLALCHEMY_DATABASE_URI='sqlite:///lostandfound.sqlite',
    SQLALCHEMY_TRACK_MODIFICATIONS=False,
    SESSION_COOKIE_SAMESITE="Lax",
    SESSION_COOKIE_SECURE=False
)

db.init_app(app)
bootstrap = Bootstrap5(app)

with app.app_context():
    db.create_all()

@app.route("/")
def start():
    return redirect(url_for("login"))

@app.route("/home")
def home():
    if "user_id" not in session:
        flash("Bitte zuerst einloggen!", "warning")
        return redirect(url_for("login"))

    posts = db.session.execute(db.select(Post)).scalars()
    return render_template("home.html", posts=posts)

from flask import request

@app.route('/register/', methods=['GET', 'POST'])
def register():

    form = forms.RegisterForm()

    print("REQUEST:", request.method)

    if request.method == "POST":
        print("FORM ERRORS:", form.errors)

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
        return redirect(url_for("contact"))

    return render_template("register.html", form=form)

@app.route("/contact/", methods=["GET","POST"])
def contact():
    form = forms.ContactForm()
    if form.validate_on_submit():
        flash("Kontakt gespeichert!", "success")

        return redirect(url_for("home"))
    return render_template("contact.html", form=form)

@app.route("/create_post", methods=["GET", "POST"])
def create_post():
    if "user_id" not in session:
        return redirect(url_for("login"))
    return render_template("create_post.html")

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

        session["user_id"] = user.user_id

        flash("Login erfolgreich!", "success")
        return redirect(url_for("home"))

    return render_template("login.html", form=form)

@app.route("/logout/")
def logout():
    session.clear()
    flash("Du bist ausgeloggt!", "info")
    return redirect(url_for("login"))
if __name__ == "__main__":
    app.run(debug=True)