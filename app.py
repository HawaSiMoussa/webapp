import os
from flask import Flask, render_template, redirect, url_for, request, flash
from flask_bootstrap import Bootstrap5
from db import db, Post
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


@app.route('/logins/', methods=['GET', 'POST'])
def login():
    form = forms.CreateLogin()  # (1.)
    if request.method == 'GET': # (3.)
            
            return render_template('login.html',form=form)
    
    else: 
            if form.validate():
               flash('Login war erfolgreich!', 'success')  # (5.)
                   
            else: 
               flash('Ihr Login war nicht möglich. Bitte versuchen sie es erneut!', 'warning')     
           
            return redirect(url_for('login'))

@app.route('/suche/', methods=['GET', 'POST']) 
def suche():
form = forms.Suchleiste()
posts = []

if request.method == 'GET':
   return render_template('suche.html', form=forms, posts=[])
 
if forms.validate_on_submit():
         suchwort = forms.suchbegriff.data

posts = db.session.execute(
     db.select(Post).where(
          Post.titel.ilike(f"%{suchwort}")
     )
        ).scalars()
return render_template('suche.html',form=forms,posts=posts)
flash('Suche ist nicht korrekt', 'warning')

return redirect(url_for('suche'))
