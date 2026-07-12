from flask import Flask, render_template, request, redirect, session, url_for, flash
import forms
import os
from db import db, Post, StandardUser
from flask_bootstrap import Bootstrap5
from flask_mail import Mail, Message

app = Flask(__name__)
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True

app.config['MAIL_USERNAME'] = 'useto.test.169@gmail.com'
app.config['MAIL_PASSWORD'] = 'famr lhrw ysyr wbvn'
app.config['MAIL_DEFAULT_SENDER'] = 'useto.test.169@gmail.com'

app.config.from_mapping(
    SECRET_KEY='secret_key_just_for_dev_environment',
    BOOTSTRAP_BOOTSWATCH_THEME='pulse',
    SQLALCHEMY_DATABASE_URI='sqlite:///lostandfound.sqlite',
    SQLALCHEMY_TRACK_MODIFICATIONS=False
)

db.init_app(app)
bootstrap = Bootstrap5(app)
mail = Mail(app)
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

@app.route("/send_fundbuero_mail/<int:post_id>/", methods=["POST"])
def send_fundbuero_mail(post_id):

    if "user_id" not in session or "fundbuero_id" not in session:
        flash("Bitte zuerst einloggen!", "warning")
        return redirect(url_for("login"))

    post = db.session.get(Post, post_id)


    if post is None:
        flash("Der Post existiert nicht.", "warning")
        return redirect(url_for("home"))
    
    if post.fundbuero_id != session["fundbuero_id"]:
        flash("Dieser Post gehört nicht zu deinem Fundbüro.", "warning")
        return redirect(url_for("home"))

    msg = Message(
        subject="Gefunden: " + post.titel,
        recipients=[post.user.hwr_mail]
    )
    msg.body = post.fundbuero.standardtext

    mail.send(msg)

    flash("Mail wurde verschickt.", "success")
    return redirect(url_for("home"))
if __name__ == "__main__":
    app.run(debug=True)