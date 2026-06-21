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
      
      
#Post erstellem
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