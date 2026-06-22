from flask import Flask, render_template, redirect, url_for, flash, session
import forms
from db import db, Post, StandardUser
from flask_bootstrap import Bootstrap5
from flask import request 
from flask import jsonify
from datetime import date, timedelta

app = Flask(__name__)

app.config.from_mapping(
    SECRET_KEY='secret_key_just_for_dev_environment',
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


@app.route("/home/")
def home():
    if "user_id" not in session:
        flash("Bitte zuerst einloggen!", "warning")
        return redirect(url_for("login"))

    posts = db.session.execute(db.select(Post).where(Post.verfallsdatum>=date.today())
                               ).scalars()
    return render_template("home.html", posts=posts)


@app.route('/register/', methods=['GET', 'POST'])
def register():

    form = forms.RegisterForm()

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

        session["user_id"] = user.user_id

        flash("Account erstellt!", "success")
        return redirect(url_for("contact"))

    return render_template("register.html", form=form)


#Kontaktformular
@app.route("/contact/", methods=["GET","POST"])
def contact():
    if "user_id" not in session:
        flash("Bitte zuerst einloggen!", "warning")
        return redirect(url_for("login"))

    form = forms.ContactForm()

    if form.validate_on_submit():

        user = db.session.get(
            StandardUser,
            session["user_id"]
        )

        user.name = form.name.data
        user.benutzername = form.username.data
        user.telefonnummer = form.phone_number.data

        db.session.commit()
        

        flash("Daten erfolgreich gespeichert!", "success")

        return redirect(url_for("home"))


    return render_template(
        "contact.html",
        form=form
    )

#Post erstellen(Fatme)
@app.route("/create/", methods=["GET", "POST"])
def create_post():

    form = forms.CreatePostForm()

    if request.method == 'GET':

        return render_template(
            'create_post.html',
            form=form
        )

    else:
#Validator
        if form.validate():

            aktiver_post = db.session.execute(
                db.select(Post).where(
                    Post.user_id == session["user_id"],
                    Post.status == "laufend"
                )
            ).scalar_one_or_none()

            if aktiver_post:
                flash(
                    "Du hast bereits eine aktive Suchanzeige.",
                    "warning"
                )
                return redirect(url_for("create_post"))
            
            heute = date.today()
            post = Post(
                user_id=session["user_id"],
                titel=form.title.data,
                beschreibung=form.description.data,
                verlustdatum=form.lost_date.data,
                verlustort=form.lost_area.data,

                meldedatum=heute,
                verfallsdatum=heute + timedelta(days=30),

                status="laufend"
            )

            db.session.add(post)
            db.session.commit()

            flash('Post erfolgreich erstellt.', 'success')

        else:

            print(form.errors)

            if 'lost_date' in form.errors:
                flash(form.errors['lost_date'][0], 'warning')

        return redirect(url_for('create_post'))


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

if __name__ == "__main__":
    app.run(debug=True)