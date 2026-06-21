
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
   

@app.route("/")
def index():

    # Read all posts from database and pass them to home.html template
    posts = db.session.execute( db.select(Post) ).scalars()

    return render_template("home.html", posts=posts)

#Kontaktformular(Fatme)
@app.route('/contact/', methods=['GET', 'POST'])
def contact():

    form = forms.ContactForm()

    if request.method == 'GET':
        return render_template('contact.html', form=form)

    else:

        if form.validate():

            user = db.session.execute(
                db.select(StandardUser)
                .order_by(StandardUser.user_id.desc())
            ).scalar()

            if user:
                user.name = form.name.data
                user.benutzername = form.username.data
                user.telefonnummer = form.phone_number.data

                db.session.commit()

                flash(
                    "Kontaktdaten erfolgreich gespeichert.",
                    "success"
                )

            else:

                flash(
                    "Kein registrierter Benutzer gefunden.",
                    "warning"
                )

        return redirect(url_for('contact'))
      

#Post erstellen(Fatme)
@app.route('/create/', methods=['GET', 'POST'])
def create_post():

    form = forms.CreatePostForm()

    if request.method == 'GET':

        return render_template(
            'create_post.html',
            form=form
        )

    else:

        if form.validate():

            post = Post(
                user_id=1,  # später durch echten Login ersetzen
                titel=form.title.data,
                beschreibung=form.description.data,
                verlustdatum=form.lost_date.data,
                verlustort=form.lost_area.data,
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
    
if __name__ == "__main__":
    app.run(debug=True)



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
