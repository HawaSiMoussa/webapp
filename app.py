from flask import Flask, render_template, redirect, url_for, flash, session
import forms
from db import db, Post, StandardUser, migrate, Campus, Fundbuero
from flask_bootstrap import Bootstrap5
from flask import request 
from flask import jsonify
from datetime import date, timedelta
import os
from flask_mail import Mail, Message
from mail import Config

app = Flask(__name__)
app.config.from_object(Config)

app.config.from_mapping( #nutzung von datenbank , sicherheit und session
    SECRET_KEY='secret_key_just_for_dev_environment',#session
    SQLALCHEMY_DATABASE_URI='sqlite:///lostandfound.sqlite',# sqlite datenbank pfad
    SQLALCHEMY_TRACK_MODIFICATIONS=False,
    SESSION_COOKIE_SAMESITE="Lax",
    SESSION_COOKIE_SECURE=False #aufgrund lokaler Entwicklung
)
 #hier mit app verknüfen
db.init_app(app) #verknüpft die datenbank mit flask app
mail = Mail(app)
migrate.init_app(app, db)
bootstrap = Bootstrap5(app)

with app.app_context():
    admins_to_create = [ # wir setzen sarahs account als den admin der dann auch sachen löchen kann etc
        {
            "hwr_mail": "s_tayem24@stud.hwr-berlin.de",
            "passwort": "Sarah12345678",
            "name": "Sarah Tayem",
            "benutzername": "Sarahtayem"
        },
    ]

    for admin_data in admins_to_create:
        exists = db.session.execute(
            db.select(StandardUser).where(StandardUser.hwr_mail == admin_data["hwr_mail"])
        ).scalar()

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

    campus_liste = ["Schöneberg", "Lichtenberg"]

    for campus_name in campus_liste:
        exists = db.session.get(Campus, campus_name)
        if not exists:
            new_campus = Campus(campus_id=campus_name, ort=campus_name)
            db.session.add(new_campus)
    db.session.commit()

    fundbueros_to_create = [
    {
        "fundbuero_id": 1,
        "campus_id": "Schöneberg",
        "raum": "Haus A, Raum A 0.31",
        "name": "Pforte Haus A",
        "telefonnummer": "+49 30 30877-1400",
        "email": "pfortea@hwr-berlin.de",
        "standardtext": (
            "Hallo,\n\n"
            "dein Gegenstand wurde bei uns abgegeben und liegt zur Abholung bereit.\n\n"
            "Pforte Haus A\n"
            "Campus Schöneberg, Haus A, Raum A 0.31\n"
            "Badensche Straße 52, 10825 Berlin\n"
            "Telefon: +49 30 30877-1400\n\n"
            "Bitte bring nach Möglichkeit einen Nachweis mit, dass der Gegenstand dir gehört.\n\n"
            "Viele Grüße\n"
            "Pforte Haus A"
        )
    },
    {
        "fundbuero_id": 2,
        "campus_id": "Schöneberg",
        "raum": "Haus B, Raum B 0.21",
        "name": "Pforte Haus B",
        "telefonnummer": "+49 30 30877-1222",
        "email": "pforteb@hwr-berlin.de",
        "standardtext": (
            "Hallo,\n\n"
            "dein Gegenstand wurde bei uns abgegeben und liegt zur Abholung bereit.\n\n"
            "Pforte Haus B\n"
            "Campus Schöneberg, Haus B, Raum B 0.21\n"
            "Badensche Straße 50-51, 10825 Berlin\n"
            "Telefon: +49 30 30877-1222\n\n"
            "Bitte bring nach Möglichkeit einen Nachweis mit, dass der Gegenstand dir gehört.\n\n"
            "Viele Grüße\n"
            "Pforte Haus B"
        )
    },
    {
        "fundbuero_id": 3,
        "campus_id": "Schöneberg",
        "raum": "Haus E, Raum E 1.09",
        "name": "Pforte Haus E",
        "telefonnummer": "+49 30 30877-1430",
        "email": "pfortee@hwr-berlin.de",
        "standardtext": (
            "Hallo,\n\n"
            "dein Gegenstand wurde bei uns abgegeben und liegt zur Abholung bereit.\n\n"
            "Pforte Haus E\n"
            "Campus Schöneberg, Haus E, Raum E 1.09\n"
            "Babelsberger Straße 14-16, 10715 Berlin\n"
            "Telefon: +49 30 30877-1430\n\n"
            "Bitte bring nach Möglichkeit einen Nachweis mit, dass der Gegenstand dir gehört.\n\n"
            "Viele Grüße\n"
            "Pforte Haus E"
        )
    },
    {
        "fundbuero_id": 4,
        "campus_id": "Lichtenberg",
        "raum": "Haus 1, Raum 1.0069",
        "name": "Hausmeister Lichtenberg",
        "telefonnummer": "+49 30 30877-2519",
        "email": "michael.boersel@hwr-berlin.de",
        "standardtext": (
            "Hallo,\n\n"
            "dein Gegenstand wurde bei uns abgegeben und liegt zur Abholung bereit.\n\n"
            "Campus Lichtenberg, Haus 1, Raum 1.0069\n"
            "Alt-Friedrichsfelde 60, 10315 Berlin\n"
            "Telefon: +49 30 30877-2519\n\n"
            "Bitte bring nach Möglichkeit einen Nachweis mit, dass der Gegenstand dir gehört.\n\n"
            "Viele Grüße\n"
            "Campus Lichtenberg"
        )
    }

         ]
    

    fundbuero_users_to_create = [
        {"hwr_mail": "pfortea@hwr-berlin.de", "passwort": "Fundbuero123456", "name": "Pforte Haus A", "benutzername": "pforte_haus_a", "fundbuero_id": 1},
        {"hwr_mail": "pforteb@hwr-berlin.de", "passwort": "Fundbuero123456", "name": "Pforte Haus B", "benutzername": "pforte_haus_b", "fundbuero_id": 2},
        {"hwr_mail": "pfortee@hwr-berlin.de", "passwort": "Fundbuero123456", "name": "Pforte Haus E", "benutzername": "pforte_haus_e", "fundbuero_id": 3},
        {"hwr_mail": "michael.boersel@hwr-berlin.de", "passwort": "Fundbuero123456", "name": "Hausmeister Lichtenberg", "benutzername": "hausmeister_lichtenberg", "fundbuero_id": 4},
    ]
    for fundbuero_daten in fundbueros_to_create:
        exists = db.session.get(Fundbuero, fundbuero_daten["fundbuero_id"])
        if not exists:
            new_fundbuero = Fundbuero(**fundbuero_daten)
            db.session.add(new_fundbuero)
    db.session.commit()


    for benutzer_daten in fundbuero_users_to_create:
        exists = db.session.execute(
            db.select(StandardUser).where(StandardUser.hwr_mail == benutzer_daten["hwr_mail"])
        ).scalar()

        if not exists:
            new_fundbuero_user = StandardUser(
                hwr_mail=benutzer_daten["hwr_mail"],
                passwort=benutzer_daten["passwort"],
                name=benutzer_daten["name"],
                benutzername=benutzer_daten["benutzername"],
                fundbuero_id=benutzer_daten["fundbuero_id"]
            )
            db.session.add(new_fundbuero_user)
    db.session.commit()

@app.route("/") # in der startseite werden die user auf die login seite weitergeleitet
def start():
    return redirect(url_for("login"))

#Feed bzw. Home Seite der zeigt alle aktuell aktiven und nicht beendete Posts an.
@app.route("/home")
def home():
    if "user_id" not in session:
        flash("Bitte zuerst einloggen!", "warning")
        return redirect(url_for("login"))
    
    form = forms.Suchleiste()
    user = db.session.get(StandardUser, session["user_id"])
    fundbuero = db.session.get(Fundbuero, session["fundbuero_id"])
    
    posts = db.session.execute(
    db.select(Post).where(
        Post.ablaufdatum >= date.today(),
        Post.status == "laufend"
    )
).scalars()

    return render_template("home.html", posts=posts, form=form, user=user, fundbuero=fundbuero)

# jetzt wird eine register funktion erstellt, die es den usern ermöglicht, sich zu registrieren. die funktion überprüft, ob die eingegebene email bereits in der datenbank existiert. wenn ja, wird eine warnung angezeigt. wenn nein, wird ein neuer user erstellt und in der datenbank gespeichert. danach wird der user automatisch eingeloggt und auf die contact seite weitergeleitet.
@app.route('/register/', methods=['GET', 'POST'])
def register():

    form = forms.RegisterForm() # objekt form der klasse register form erstellt 
    # hier wird überprüft, ob das formular korrekt ausgefüllt wurde. wenn ja, wird der user erstellt und in der datenbank gespeichert. wenn nein, wird das formular erneut angezeigt.
    if form.validate_on_submit():
        

        existing_user = db.session.execute(
            db.select(StandardUser).where(
                StandardUser.hwr_mail == form.hwrmail.data
            )
        ).scalars()

        if len(list(existing_user)) > 0: # hier wird überprüft, ob die eingegebene email bereits in der datenbank existiert. wenn ja, wird eine warnung angezeigt und der user wird auf die register seite weitergeleitet.
            flash("Diese E-Mail wird bereits verwendet!", "warning")
            return redirect(url_for("register"))

        user = StandardUser( # hier wird ein neuer user erstellt und in der datenbank gespeichert.
            hwr_mail=form.hwrmail.data,
            passwort=form.passwort.data,
            campus_id=form.campus.data,
            is_admin=False
     )


        db.session.add(user)
        db.session.commit()

        session["user_id"] = user.user_id
        session["campus_id"] = user.campus_id
        session["is_admin"] = False

        flash("Account erstellt!", "success")
        return redirect(url_for("contact"))
    
    

    return render_template("register.html", form=form)


#Kontaktformular hier kann der user seine kontaktinformationen eingeben. die funktion überprüft, ob der user eingeloggt ist. wenn ja, wird das formular angezeigt. wenn nein, wird der user auf die login seite weitergeleitet.
@app.route("/contact/", methods=["GET","POST"])
def contact():
    if "user_id" not in session: #existiert die session des eingeloggten users nicht, wird er auf die login seite weitergeleitet.
        flash("Bitte zuerst einloggen!", "warning")
        return redirect(url_for("login"))

    form = forms.ContactForm()

    if form.validate_on_submit(): #erst bei POST 

        user = db.session.get( #User Objekt erstellt über
            StandardUser,
            session["user_id"]
        )

        user.name = form.name.data
        user.benutzername = form.username.data
        user.telefonnummer = form.phone_number.data

        db.session.commit() #Eingabe an DB geschickt
        

        flash("Daten erfolgreich gespeichert!", "success")

        return redirect(url_for("home"))


    return render_template(
        "contact.html",
        form=form
    )

# der user kann hier eine neue suchanzeige erstellen. die funktion überprüft, ob der user eingeloggt ist. wenn ja, wird das formular angezeigt. wenn nein, wird der user auf die login seite weitergeleitet.
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
          if not session.get("is_admin"): #HAWA -->session.get("is_admin") überprüft, ob der eingeloggte user ein admin ist. wenn ja, wird er auf die home seite weitergeleitet. wenn nein, wird er auf die create_post seite weitergeleitet.
            aktiver_post = db.session.execute(
                db.select(Post).where(
                    Post.user_id == session["user_id"],
                    Post.status == "laufend" 
                )
            ).scalar() 

            if aktiver_post:
                flash(
                    "Du hast bereits eine aktive Suchanzeige.",
                    "warning"
                )
                return redirect(url_for("create_post"))
            # das heutige datum wird hier gespeichert, damit es später für die ablaufdatum berechnung verwendet werden kann.
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
 # es wird überprüft, ob das formular korrekt ausgefüllt wurde. wenn nicht, werden die fehler angezeigt.
            print(form.errors)

            if 'lost_date' in form.errors:
                flash(form.errors['lost_date'][0], 'warning')
                
        return redirect(url_for('create_post'))
    
# die anzeige kann hier geschlossen werden, wenn der user sein gegenstand gefunden hat.  der status des posts wird auf "gefunden" gesetzt und der post wird in der datenbank gespeichert. Momentan fehlt noch user check
@app.route ("/close_post/<int:post_id>/")
#grad nur auf get gesetzt muss aber post sein, weil am status was geändert wird
def close_post(post_id):
    post = db.session.get(Post, post_id)

    post.status ="gefunden"
 

    db.session.commit()

    flash( "Es freut uns, dass du dein Gegenstand finden konntest! Dein Post wurde geschlossen.", "success") #success: grüner kasten
    
    return redirect (url_for("profile"))

@app.route('/login/', methods=['GET', 'POST'])
def login(): # in diesem teil wird die login funktion erstellt. die funktion überprüft, ob der user eingeloggt ist. wenn ja, wird er auf die home seite weitergeleitet. wenn nein, wird das formular angezeigt. wenn das formular korrekt ausgefüllt wurde, wird der user eingeloggt und auf die home seite weitergeleitet. wenn das formular nicht korrekt ausgefüllt wurde, wird eine warnung angezeigt und der user bleibt auf der login seite.

    form = forms.CreateLogin() # Nimm das Formular aus forms.py und zeige 

    if form.validate_on_submit():

        user = db.session.execute( # execute führt die sql abfrage aus und gibt ein result object zurück
            db.select(StandardUser).where( #in tabelle standarduser reun
                StandardUser.hwr_mail == form.hwrmail.data # nimm von der Tabelle alle user dessen hwr mail mit der hwrmail übereinstimmt, die der user im formular eingegeben hat. wenn es keinen user gibt, der diese hwrmail hat, wird None zurückgegeben.
            )
        ).scalar() # s weg machen überarbeiten dann geht wohl der fehler

        if user is None:
            flash("User existiert nicht.", "warning")
            return redirect(url_for("login"))

        if user.passwort != form.passwort.data:
            flash("Falsches Passwort!", "warning")
            return redirect(url_for("login"))

        session["user_id"] = user.user_id
        session["is_admin"] = user.is_admin
        session ["fundbuero_id"] = user.fundbuero_id

        flash("Login erfolgreich!", "success")
        return redirect(url_for("home"))

    return render_template("login.html", form=form)

#zeigt die daten des eingeloggten users an. die funktion überprüft, ob der user eingeloggt ist. wenn ja, werden die daten des users angezeigt. wenn nein, wird der user auf die login seite weitergeleitet.
@app.route('/profile/')
def profile():
    if "user_id" not in session:
        flash("Bitte zuerst einloggen!", "warning")
        return redirect(url_for("login"))
    
    user = db.session.get(StandardUser, session["user_id"] ) 

    posts = db.session.execute( db.select(Post).where(Post.user_id == user.user_id, Post.status == "laufend")).scalars() # das holt alle posts des eingeloggten users aus der datenbank, die noch nicht abgelaufen sind und deren status "laufend" ist. die posts werden dann in der profile.html datei angezeigt.
    return render_template("profile.html", user=user, posts= posts)


# Profil bearbeiten es ermöglicht daas ändenrn der benutzerinformationen. 
@app.route('/profile/edit/', methods=['GET', 'POST'])
def edit_profile():

    if "user_id" not in session:
        flash("Bitte zuerst einloggen!", "warning")
        return redirect(url_for("login"))
# Instanz der Klasse StandardUser mit der user_id aus der session wird hier erstellt. 
    user = db.session.get(
        StandardUser,
        session["user_id"]
    )#
    #obj ist ein parameter aus der flaskforms bibliothek
    form = forms.EditProfileForm(obj=user) #obj=user sorgt dafür, dass die aktuellen daten des users im formular angezeigt werden, wenn die seite geladen wird
    if form.validate_on_submit(): # wenn das formular korrekt ausgefüllt wurde

        user.benutzername = form.benutzername.data
        user.name = form.name.data
        user.telefonnummer = form.telefonnummer.data
        user.campus_id = form.campus_id.data
# .data repräsentiert die daten, die der user im formular eingegeben hat. 
        flash(
            "Profil erfolgreich aktualisiert!",
            "success"
        )
    
        return redirect(url_for("profile"))
# wird in zwei fällen ausgeführt: wenn das formular nicht korrekt ausgefüllt wurde oder wenn die seite zum ersten mal geladen wird. 
    return render_template(
        "edit_profile.html",
        form=form
    )

@app.route("/logout") # löscht die session des eingeloggten users und leitet ihn auf die login seite weiter.
def logout():

    session.pop("user_id", None)

    flash( "Erfolgreich ausgeloggt.", "success")

    return redirect(url_for("login"))


@app.route("/api/posts") # gitb alle posts in der datenbank als json zurück. 
def api_posts():

    posts = db.session.execute(
        db.select(Post)
    ).scalars()
#jsonify gibt die daten als json zurück. die daten werden in einer liste gespeichert, die dann in der api_posts.html datei angezeigt wird. die daten werden in einem dictionary gespeichert, das dann in der liste gespeichert wird
#also: python datenstruktur(liste von dictionaries)--> json string--> in flask response objekt verpackt
    return jsonify([ 
        {
            "titel": p.titel,
            "status": p.status
        }
        for p in posts
    ])

@app.route ("/edit_post/<int:post_id>/", methods= ["GET", "POST"])
def edit_post (post_id):

    post = db.session.get(Post,post_id)
    if not post:
         return redirect(url_for("home"))

    if post.user_id != session["user_id"] and not session.get("is_admin"):
        flash("Du hast keine Berechtigung, diesen Post zu bearbeiten.", "warning")
        return redirect(url_for("home"))


    form = forms.CreatePostForm()# suchanzeige bearbeuten auch für später

    if request.method == "GET":
        form.title.data = post.titel
        form.description.data = post.beschreibung
        form.lost_date.data = post.verlustdatum
        form.lost_area.data = post.verlustort

    if form.validate_on_submit():

        post.titel = form.title.data
        post.beschreibung = form.description.data
        post.verlustdatum = form.lost_date.data
        post.verlustort = form.lost_area.data
        db.session.commit()
        flash('Post erfolgreich aktualisiert.','success')
        return redirect(url_for('profile')) # alte daten werden vorbeigeschickt und die neuen daten werden in der datenbank gespeichert.
    
    return render_template('edit_post.html',form=form)

@app.route("/search", methods=["GET", "POST"])
def suche(): 
    form = forms.Suchleiste() 
    posts = []
    user = db.session.get(StandardUser, session.get("user_id"))

    if form.validate_on_submit():
        suchbegriff = form.suchfeld.data
        result = db.session.execute(
            db.select(Post).where(
                Post.titel.contains(suchbegriff) | Post.beschreibung.contains(suchbegriff)
            )
        ).scalars()
        posts = list(result)

    return render_template("suche.html", posts=posts, form=form, user=user)

@app.route("/delete_post/<int:post_id>/") 
def delete_post(post_id):
    if "user_id" not in session:
        flash("Bitte zuerst einloggen!", "warning")
        return redirect(url_for("login"))
    
    post = db.session.get(Post, post_id)
    if not post:
        flash("Post nicht gefunden.", "warning")
        return redirect(url_for("home"))
    
    # Berechtigungsprüfung
    is_admin = session.get("is_admin") == True
    is_owner = (post.user_id == session.get("user_id"))

    if is_owner or is_admin:
        db.session.delete(post)
        db.session.commit()
        flash("Der Post wurde erfolgreich gelöscht.", "success")
    else: 
        flash("Du hast keine Berechtigung, diesen Post zu löschen.", "warning")

    return redirect(url_for("home"))

@app.route("/post/<int:post_id>/")
def post_detail(post_id):
    if "user_id" not in session:
        flash("Bitte zuerst einloggen!", "warning")
        return redirect(url_for("login"))

    post = db.session.get(Post, post_id)

    if post is None:
        flash("Diesen Post gibt es nicht (mehr).", "warning")
        return redirect(url_for("home"))

    post.views = (post.views or 0) + 1
    db.session.commit()

    return render_template("post_detail.html", post=post)

   
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

@app.route("/fundbuero/")
def fundbuero_dashboard():
    if "fundbuero_id" not in session or session["fundbuero_id"] is None:
        flash("Bitte zuerst einloggen!", "warning")
        return redirect(url_for("login"))

    fundbuero = db.session.get(Fundbuero, session["fundbuero_id"])

    posts = db.session.execute(
        db.select(Post).where(
            Post.fundbuero_id == session["fundbuero_id"],
            Post.status == "laufend"
        )
    ).scalars()

@app.route("/dev/reset_fundbueros/")
def reset_fundbueros():
    db.session.execute(
        db.delete(StandardUser).where(StandardUser.fundbuero_id.isnot(None))
    )
    db.session.execute(db.delete(Fundbuero))
    db.session.commit()

    return "Fundbüro-Daten gelöscht. Starte die App neu (Strg+C, dann python app.py erneut), damit der Seed-Code sie neu anlegt."
    return render_template("profile_fb.html", fundbuero=fundbuero, posts=posts)
    # alles starten
if __name__ == "__main__":
    app.run(debug=True)
