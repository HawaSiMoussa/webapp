import os
from flask import Flask, render_template, redirect, url_for, request, flash
import forms 

app = Flask(__name__)
app.config.from_mapping(
    SECRET_KEY='secret_key_just_for_dev_environment')
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

if __name__ == "__main__":
    app.run(debug=True)


@app.route('/logins/', methods=['GET', 'POST'])
def login():
    form = forms.CreateLogin()  # (1.)
    if request.method == 'GET':
        return render_template('login.html')  # (2.)
    else:  # request.method == 'POST'
        if form.validate():  # (3.)
            flash('Login war erfolgreich!', 'success')  # (5.)
        else:
            flash('Ihr Login war nicht möglich. Bitte versuchen sie es erneut!', 'warning')
        return redirect(url_for('login'))