from flask import Flask, render_template, redirect, url_for, flash, session
import forms
from db import db, Post, StandardUser, migrate
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
migrate.init_app(app, db)
bootstrap = Bootstrap5(app)

with app.app_context():
    db.create_all()

    admins_to_create = [
        {
            "hwr_mail": "s_tayem24@stud.hwr-berlin.de",
            "passwort": "Sarah12345678",
            "name": "Sarah Tayem",
            "benutzername": "Sarahtayem"
        },
        {
            "hwr_mail": "fabian.rauchholz@hwr-berlin.de",
            "passwort": "Fabian12345678",
            "name": "Fabian Rauchholz",
            "benutzername": "FabianLichtenberg"
        },
        {
            "hwr_mail": "verena.dikof@hwr-berlin.de",
            "passwort": "Verena12345678",
            "name": "Verena Dikof",
            "benutzername": "VerenaLichtenberg"
        },
        {
            "hwr_mail": "pforteb@hwr-berlin.de",
            "passwort": "Pforte12345678",
            "name": "Pförtner Haus A, B, E",
            "benutzername": "PforteSchoeneberg"
        }
    ]

    for admin_data in admins_to_create:
        # Prüfen, ob der Admin schon in der DB existiert
        exists = db.session.execute(
            db.select(StandardUser).where(StandardUser.hwr_mail == admin_data["hwr_mail"])
        ).scalar_one_or_none()

        
        if not exists:
            new_admin = StandardUser(
                hwr_mail=admin_data["hwr_mail"],
                passwort=admin_data["passwort"],
                name=admin_data["name"],
                benutzername=admin_data["benutzername"],
                is_admin=True
            )
            db.session.add(new_admin)

    db.session.commit()

@app.route("/")
def start():
    return redirect(url_for("login"))


#Feed bzw. Home Seite
@app.route("/home")
def home():

    if "user_id" not in session:

        flash("Bitte zuerst einloggen!", "warning")

        return redirect(url_for("login"))
    form = forms.Suchleiste()

    user = db.session.get(StandardUser,session["user_id"])

    posts = db.session.execute(db.select(Post).where(Post.ablaufdatum>=date.today())
                               ).scalars()
    return render_template("home.html", posts=posts, form=form, user=user)


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
                ablaufdatum=heute + timedelta(days=30),

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
    

@app.route("/post/delete/<int:post_id>")
def delete_post(post_id):

    post = db.session.get(Post, post_id)

    if post is None:
        flash("Post nicht gefunden", "warning")
        return redirect(url_for("home"))

    if not session.get("is_admin"):
        flash("Keine Berechtigung!", "danger")
        return redirect(url_for("home"))

    db.session.delete(post)
    db.session.commit()

    flash("Post gelöscht", "success")
    return redirect(url_for("home"))


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
        session["is_admin"] = user.is_admin

        flash("Login erfolgreich!", "success")
        return redirect(url_for("home"))

    return render_template("login.html", form=form)

#Profil anzeigen
@app.route('/profile/')
def profile():
    if "user_id" not in session:
        flash("Bitte zuerst einloggen!", "warning")
        return redirect(url_for("login"))
    
    user = db.session.get(StandardUser, session["user_id"] ) 

    posts = db.session.execute( db.select(Post).where(Post.user_id == user.user_id, Post.status == "laufend")).scalars()
    return render_template("profile.html", user=user, posts= posts)


# Profil bearbeiten
@app.route('/profile/edit/', methods=['GET', 'POST'])
def edit_profile():

    if "user_id" not in session:
        flash("Bitte zuerst einloggen!", "warning")
        return redirect(url_for("login"))

    user = db.session.get(
        StandardUser,
        session["user_id"]
    )
    form = forms.EditProfileForm(obj=user)
    if form.validate_on_submit():

        user.benutzername = form.benutzername.data
        user.name = form.name.data
        user.telefonnummer = form.telefonnummer.data
        user.campus_id = form.campus_id.data

        db.session.commit()

        flash(
            "Profil erfolgreich aktualisiert!",
            "success"
        )
    
        return redirect(url_for("profile"))

    return render_template(
        "edit_profile.html",
        form=form
    )

@app.route("/logout")
def logout():

    session.pop("user_id", None)

    flash( "Erfolgreich ausgeloggt.", "success")

    return redirect(url_for("login"))


@app.route("/api/posts")
def api_posts():

    posts = db.session.execute(
        db.select(Post)
    ).scalars()

    return jsonify([
        {
            "titel": p.titel,
            "status": p.status
        }
        for p in posts
    ])

@app.route ("/close_post/<int:post_id>/")
def close_post(post_id):
    post = db.session.get(Post, post_id)

    post.status ="gefunden"

    db.session.commit()

    flash( "Es freut uns, dass du dein Gegenstand finden konntest! Dein Post wurde geschlossen.", "success") #success: grüner kasten
    
    return redirect (url_for("profile"))

@app.route ("/edit_post/<int:post_id>/", methods= ["GET", "POST"])
def edit_post (post_id):

    post = db.session.get(Post,post_id)

    form = forms.CreatePostForm()
    if request.method == 'GET':

            form.title.data = post.titel
            form.description.data = post.beschreibung
            form.lost_date.data = post.verlustdatum
            form.lost_area.data = post.verlustort

            return render_template('edit_post.html',form=form)
    else:

            if form.validate():

                post.titel = form.title.data
                post.beschreibung = form.description.data
                post.verlustdatum = form.lost_date.data
                post.verlustort = form.lost_area.data

                db.session.commit()

                flash('Post erfolgreich aktualisiert.','success')
            else:

                flash('Post konnte nicht aktualisiert werden.','warning'
                )

            return redirect(url_for('profile'))


if __name__ == "__main__":
    app.run(debug=True)