import os
from flask import Flask, render_template, redirect, url_for, request, flash
from flask_bootstrap import Bootstrap5
from db import db, Post, StandardUser
import forms 

app = Flask(__name__)

app.config['SECRET_KEY'] = 'secret_key_just_for_dev_environment'
app.config['SQLALCHEMY_DATABASE_URI'] ='sqlite:///lostandfound.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
 
bootstrap = Bootstrap5(app)
db.init_app(app)
with app.app_context():
    db.create_all()
     

title = "LostAndFound"
group = "CampusFinder"

members = [
    "77204183234, Hawa Si Moussa",
    "77209887107, Fatme Berjaoui",
    "77209886771, Sarah Tayem"
]

tasks= [
    "Hawa: Benutzeroberfläche Login button posts Darstellung mit HTML, CSS",
    "Fatme: Git hub Repo's ( pull commit push und aufgaben zusammenfügen), Organisieren/dokumentieren der verschiedenen Ideen",
    "Sarah: Datenbankverwaltung (Nutzer und Beiträge), sowie Analyse geplanter Funktionen bezüglich technischer Machbarkeit und Aufwand"
]

@app.route("/")
def index():
    return render_template(
        "index.html",
        title=title,
        group=group,
        members=members,
        tasks=tasks
    )

import os
from flask import Flask, render_template, redirect, url_for, request, flash
from flask_bootstrap import Bootstrap5
from db import db, Post, StandardUser
import forms 

app = Flask(__name__)

app.config['SECRET_KEY'] = 'secret_key_just_for_dev_environment'
app.config['SQLALCHEMY_DATABASE_URI'] ='sqlite:///lostandfound.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
 
bootstrap = Bootstrap5(app)
db.init_app(app)
with app.app_context():
    db.create_all()
     

title = "LostAndFound"
group = "CampusFinder"

members = [
    "77204183234, Hawa Si Moussa",
    "77209887107, Fatme Berjaoui",
    "77209886771, Sarah Tayem"
]

tasks= [
    "Hawa: Benutzeroberfläche Login button posts Darstellung mit HTML, CSS",
    "Fatme: Git hub Repo's ( pull commit push und aufgaben zusammenfügen), Organisieren/dokumentieren der verschiedenen Ideen",
    "Sarah: Datenbankverwaltung (Nutzer und Beiträge), sowie Analyse geplanter Funktionen bezüglich technischer Machbarkeit und Aufwand"
]

@app.route("/")
def index():
    return render_template(
        "index.html",
        title=title,
        group=group,
        members=members,
        tasks=tasks
    )

@app.route('/register/', methods=['GET', 'POST'])
def register(): 
    form = forms.RegisterForm()  # (1.)
if request.method == 'POST':
 if forms.validate_on_submit():
    existing_user = db.session.execute(
        db.select(StandardUser).where(
            StandardUser.hwr_mail == forms.hwrmail.data
        )
          ).scalar_one_or_none()
if existing_user:
    flash("Diese E-Mail wird bereits verwendet!","warning")
return redirect(url_for("register"))
user= StandardUser(
        hwr_mail=forms.hwrmail.data,
        passwort=forms.password.data
    )
db.session.add(user)

db.session.commit()

flash("Account erstellt!", "success")
return redirect(url_for("login"))
return render_template("register.html",form=forms)



@app.route('/logins/', methods=['GET', 'POST'])
def login():

form = forms.CreateLogin()  # (1.)
if forms.validate_on_submit():
    user = db.session.execute(
db.select(StandardUser).where(StandardUser.hwr_mail == forms.hwrmail.data)

    ).scalar_one_or_none()
if not user: 
        flash ("User existiert nicht", "warning")
        return redirect(url_for("login"))
    
if user.passwort != form.passwort.data:
        flash ("Falsches Passwort!","warning")
        return redirect(url_for("login"))
    
        flash("Login erfolgreich!","success")
        return redirect(url_for("index"))

        return render_template("login-html", form=forms)                 
      
@app.route('/suche/', methods=['GET', 'POST'])
def suche():
    form = forms.Suchleiste()

    posts=[]

    if form.validate_on_submit():
        suchwort = form.suchbegriff.data

        posts = db.session.execute(
            db.select(Post).where(
                Post.titel.ilike(f"%{suchwort}%")
            )
        ).scalars().all()

    if request.method == 'GET':
        return render_template(
            'suche.html',
            form=form,
            posts=[]
        )
    if form.validate_on_submit():
        suchwort = form.suchbegriff.data

        posts = db.session.execute(
            db.select(Post).where(
                Post.titel.ilike(f"%{suchwort}%")
            )
        ).scalars().all()

    return render_template(
            'suche.html',
            form=form,
            posts=posts
        )

@app.route('/suche/', methods=['GET', 'POST'])
def suche():
    form = forms.Suchleiste()

    posts=[]
        

    if form.validate_on_submit():
        suchwort = form.suchbegriff.data

        posts = db.session.execute(
            db.select(Post).where(
                Post.titel.ilike(f"%{suchwort}%")
            )
        ).scalars().all()

    if request.method == 'GET':
        return render_template(
            'suche.html',
            form=form,
            posts=[]
        )

    if form.validate_on_submit():
        suchwort = form.suchbegriff.data

        posts = db.session.execute(
            db.select(Post).where(
                Post.titel.ilike(f"%{suchwort}%")
            )
        ).scalars().all()


    return render_template(
            'suche.html',
            form=form,
            posts=posts
        )