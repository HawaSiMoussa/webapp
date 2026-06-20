from flask import Flask,render_template, request, redirect, url_for, flash
import forms
from instance.db import db, Post
from flask_bootstrap import Bootstrap5


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///lostandfound.sqlite'

app.config.from_mapping(
    SECRET_KEY='secret_key_just_for_dev_environment',
    #DATABASE=os.path.join(app.instance_path, 'todos.sqlite')
    BOOTSTRAP_BOOTSWATCH_THEME = 'pulse'
)
#Bootstrap implementieren
#app.config['SECRET_KEY'] = 'lostandfound123'

bootstrap = Bootstrap5(app)
db.init_app(app)

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

#Kontaktformular
@app.route('/contact/', methods=['GET', 'POST'])
def contact():

    form=forms.ContactForm()
    if request.method == 'GET':
        return render_template('contact''.html',form=form)
    else:
      if form.validate():
        print(form.name.data)
        print(form.username.data)
        print(form.phone_number.data)

        return redirect(
            url_for('contact')
        )

# Post erstellen
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
                user_id=1,  # vorläufig bis Login angebunden ist
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

            flash(
                'Es konnte kein Post erstellt werden.: validation error.',
                'warning'
            )

        return redirect(url_for('create_post'))
            
with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(debug=True)