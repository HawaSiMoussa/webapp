from flask import Flask, render_template, redirect, url_for, flash, session
import forms
from db import db, Post, StandardUser, migrate
from flask_bootstrap import Bootstrap5
from flask import request 
from flask import jsonify
from datetime import date, timedelta

app = Flask(__name__)

app.config.from_mapping( #nutzung von datenbank , sicherheit und session
    SECRET_KEY='secret_key_just_for_dev_environment',#session
    SQLALCHEMY_DATABASE_URI='sqlite:///lostandfound.sqlite',# sqlite datenbank pfad
    SQLALCHEMY_TRACK_MODIFICATIONS=False,
    SESSION_COOKIE_SAMESITE="Lax",
    SESSION_COOKIE_SECURE=False #aufgrund lokaler Entwicklung
)
 #hier mit app verknüfen
db.init_app(app) #verknüpft die datenbank mit flask app
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
    ]

    for admin_data in admins_to_create:
        # Hier muss 'hwr_mail' stehen, so wie es in deiner DB-Klasse heißt
        exists = db.session.execute(
            db.select(StandardUser).where(StandardUser.hwr_mail == admin_data["hwr_mail"])
        ).scalar()
        
        if not exists:
            new_admin = StandardUser(
                hwr_mail=admin_data["hwr_mail"], # Hier auch 'hwr_mail'
                passwort=admin_data["passwort"],
                name=admin_data["name"],
                benutzername=admin_data["benutzername"],
                is_admin=True
            )
            db.session.add(new_admin)
    db.session.commit()


@app.route("/") # in der startseite werden die user auf die login seite weitergeleitet
def start():
    return redirect(url_for("login"))

#Feed bzw. Home Seite der zeigt alle aktuell aktiven und nicht beendete Posts an.
@app.route("/home")
def home():
# nur die eingeloggten user können die home seite sehen, sonst werden sie auf die login seite weitergeleitet:
    if "user_id" not in session:

        flash("Bitte zuerst einloggen!", "warning")
        return redirect(url_for("login"))
    form = forms.Suchleiste()
    user = db.session.get(StandardUser,session["user_id"])
    
    posts = db.session.execute(db.select(Post).where(Post.ablaufdatum>=date.today(), Post.status == "laufend")
                           ).scalars()  # hier werden alle posts aus der datenbank geholt, die noch nicht abgelaufen sind und deren status "laufend" ist. die posts werden dann in der home.html datei angezeigt.



    return render_template("home.html", posts=posts, form=form, user=user)

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
           campus_id=form.campus.data
        )

        db.session.add(user)
        db.session.commit()

        session["user_id"] = user.user_id
        session["campus_id"] = user.campus_id

        flash("Account erstellt!", "success")
        return redirect(url_for("contact"))
    
    

    return render_template("register.html", form=form)

@app.route("/contact/", methods=["GET","POST"])
def contact():
    if "user_id" not in session:
        flash("Bitte zuerst einloggen!", "warning")
        return redirect(url_for("login"))

    form = forms.ContactForm()

    if form.validate_on_submit():
        user = db.session.get(StandardUser, session["user_id"])

        user.name = form.name.data
        user.benutzername = form.username.data
        user.telefonnummer = form.phone_number.data

        # --- HIER DER CHECK ---
        # Wir suchen nach einem anderen User, der denselben Benutzernamen hat
        doppelter_user = db.session.execute(
            db.select(StandardUser).where(StandardUser.benutzername == user.benutzername)
        ).scalar()

        # Wenn wir einen finden, der NICHT der aktuell eingeloggte User ist -> Fehler!
        if doppelter_user and doppelter_user.user_id != user.user_id:
            flash("Dieser Benutzername ist leider schon vergeben!", "danger")
            return render_template("contact.html", form=form)

        # --- DANN ERST SPEICHERN ---
        db.session.commit() 
        flash("Daten erfolgreich gespeichert!", "success")
        return redirect(url_for("home"))

    # Wenn es ein GET-Request ist, laden wir die bestehenden Daten in das Formular
    elif request.method == "GET":
        user = db.session.get(StandardUser, session["user_id"])
        form.name.data = user.name
        form.username.data = user.benutzername
        form.phone_number.data = user.telefonnummer

    return render_template("contact.html", form=form)

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

from werkzeug.security import check_password_hash
from flask import flash, redirect, url_for, session, render_template

@app.route('/login/', methods=['GET', 'POST'])
def login():
    # Wir greifen direkt auf forms.CreateLogin zu
    form = forms.CreateLogin() 
    
    if request.method == 'POST':
        print("Versuch Login für: " + str(form.hwrmail.data))
        user = db.session.execute(
            db.select(StandardUser).where(StandardUser.hwr_mail == form.hwrmail.data)
        ).scalar()
        
        if user:
            print("User gefunden: " + str(user.name))
        else:
            print("User nicht in DB gefunden!")

    if form.validate_on_submit():
        user = db.session.execute(
            db.select(StandardUser).where(StandardUser.hwr_mail == form.hwrmail.data)
        ).scalar()
        
        # Vergleich OHNE Hashing (so wie du es wahrscheinlich gelernt hast)
        if user and user.passwort == form.passwort.data:
            session["user_id"] = user.user_id
            session["is_admin"] = user.is_admin
            flash("Login erfolgreich!", "success")
            return redirect(url_for("home"))
        else:
            flash("E-Mail oder Passwort falsch!", "danger")
            
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
    
    # Debugging: Was steht in der Session?
    print(f"DEBUG: UserID in Session: {session.get('user_id')}")
    print(f"DEBUG: Ist Admin? {session.get('is_admin')}")
    print(f"DEBUG: PostUserID: {post.user_id}")

    # Berechtigungsprüfung
    is_admin = session.get("is_admin") is True
    is_owner = (post.user_id == session.get("user_id"))

    if is_owner or is_admin:
        db.session.delete(post)
        db.session.commit()
        flash("Der Post wurde erfolgreich gelöscht.", "success")
    else: 
        flash("Du hast keine Berechtigung, diesen Post zu löschen.", "warning")

    return redirect(url_for("home"))


if __name__ == "__main__":
     app.run(debug=True)
