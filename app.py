from flask import Flask, render_template, redirect, url_for, flash
from flask_bootstrap import Bootstrap5
from db import db, Post, StandardUser
import forms

app = Flask(__name__)

app.config['SECRET_KEY'] = 'secret_key_just_for_dev_environment'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///lostandfound.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

bootstrap = Bootstrap5(app)

db.init_app(app)

with app.app_context():
    db.create_all()



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

    return render_template("register.html", form=form)


@app.route('/logins/', methods=['GET', 'POST'])
def login():

    form = forms.CreateLogin()

    if form.validate_on_submit():

        if not form.hwrmail.data.endswith(
            (
                "@hwr-berlin.de",
                "@stud.hwr-berlin.de",
                "@dot.hwr-berlin.de"
            )
        ):
            flash("Bitte eine gültige HWR-Mail angeben.", "warning")
            return redirect(url_for("register"))

        user = db.session.execute(
            db.select(StandardUser).where(
                StandardUser.hwr_mail == form.hwrmail.data
            )
        ).scalar_one_or_none()

        if not user:
            flash("User existiert nicht.", "warning")
            return redirect(url_for("login"))

        if user.passwort != form.passwort.data:
            flash("Falsches Passwort!", "warning")
            return redirect(url_for("login"))

        flash("Login erfolgreich!", "success")
        return redirect(url_for("index"))

    return render_template("login.html", form=form)


@app.route('/suche/', methods=['GET', 'POST'])
def suche():

    form = forms.Suchleiste()
    posts = []

    if form.validate_on_submit():

        suchwort = form.suchbegriff.data

        posts = db.session.execute(
            db.select(Post).where(
                Post.titel.ilike(f"%{suchwort}%")
            )
        ).scalars().all()

    return render_template(
        "suche.html",
        form=form,
        posts=posts
    )


if __name__ == "__main__":
    app.run(debug=True)
    