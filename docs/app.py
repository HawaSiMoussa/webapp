from flask import Flask,render_template

app = Flask(__name__)

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
import os
from flask import Flask, render_template, redirect, url_for, request, abort, flash
import db, forms

app = Flask(__name__)

app.config.from_mapping(
    SECRET_KEY='secret_key_just_for_dev_environment',
    DATABASE=os.path.join(app.instance_path, 'todos.sqlite')
)

# [...]

@app.route('/todos/', methods=['GET', 'POST'])
def todos():
    db_con = db.get_db_con()
    form = forms.CreateTodoForm()  # (1.)
    if request.method == 'GET':
        sql_query = 'SELECT * FROM todo ORDER BY id;'
        todos = db_con.execute(sql_query).fetchall()
        return render_template('todos.html', todos=todos, form=form)  # (2.)
    else:  # request.method == 'POST'
        if form.validate():  # (3.)
            sql_query = 'INSERT INTO todo (description) VALUES (?);'
            db_con.execute(sql_query, [form.description.data])  # (4.)
            db_con.commit()
            flash('Todo has been created.', 'success')  # (5.)
        else:
            flash('No todo creation: validation error.', 'warning')
        return redirect(url_for('todos'))

# [...]

