from flask import Flask,render_template
import forms
from flask import request

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

# Post erstellen
@app.route('/create/', methods=['GET', 'POST'])
def create_post():
    #db_con = db.get_db_con()
    form= forms.CreatePostForm()

    if request.method == 'GET':
        #sql_query = 'SELECT * FROM todo ORDER BY id;'
        #create_post = db_con.execute(sql_query).fetchall()
        return render_template('create_post.html',form=form) #Instanz wird automatisch mit Daten aus request.form gefüllt
           
    else :
        if form.validate():
           #sql_query = 'INSERT INTO todo (description) VALUES (?);' 
           print(form.title.data)
           print(form.descrption.data)
           print(form.lost_date.data)   #TEST
           print(form.lost_area.data)
           flash('Psot created succesfully.', 'congrats')
        else:
            flash('No todo creation: validation error.', 'warning')

        return redirect(url_for('create_post'))
            
            


