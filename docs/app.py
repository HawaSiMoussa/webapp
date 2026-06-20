from flask import Flask,render_template, request, redirect, url_for, flash
import forms
from flask_bootstrap import Bootstrap5


app = Flask(__name__)

app.config.from_mapping(
    SECRET_KEY='secret_key_just_for_dev_environment',
    #DATABASE=os.path.join(app.instance_path, 'todos.sqlite')
    BOOTSTRAP_BOOTSWATCH_THEME = 'pulse'
)
#Bootstrap implementieren
#app.config['SECRET_KEY'] = 'lostandfound123'

bootstrap = Bootstrap5(app)

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
<<<<<<< HEAD
    
=======


>>>>>>> 69012f8b8a3269225c3627e6b86f50f43439b798
