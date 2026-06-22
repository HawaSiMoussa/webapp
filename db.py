
from flask_sqlalchemy import SQLAlchemy
from datetime import date, timedelta
db = SQLAlchemy()
 


db = SQLAlchemy() #create SQLAlchemy object to be able to use it in other files, e.g. to define the data model in db.py

class Campus(db.Model):

    __tablename__ = "campus"
    campus_id = db.Column(db.String, primary_key=True)

    ort = db.Column(db.String, nullable=False)

    users = db.relationship( "StandardUser", back_populates="campus")

    fundbueros = db.relationship("Fundbuero",back_populates="campus")


class StandardUser(db.Model):
    
    __tablename__ = "standardUser"

    user_id = db.Column( db.Integer, primary_key=True )

    campus_id = db.Column( db.String, db.ForeignKey("campus.campus_id") )

    name = db.Column( db.String)

    benutzername = db.Column( db.String, unique=True)

    telefonnummer = db.Column(db.String)

    standardtext = db.Column(db.Text)

    passwort = db.Column(db.String,nullable=False)

    hwr_mail = db.Column(db.String, unique=True,nullable=False ) 

    is_admin = db.Column(db.Boolean, default=False)

    campus = db.relationship("Campus",back_populates="users")

    posts = db.relationship( "Post",back_populates="user")
   
class Fundbuero(db.Model):

    __tablename__ = "fundbuero"

    fundbuero_id = db.Column(db.Integer,primary_key=True)

    campus_id = db.Column(db.String,db.ForeignKey("campus.campus_id"))

    raum = db.Column(db.String)

    name = db.Column(db.String)

    telefonnummer = db.Column(db.String)

    email = db.Column(db.String)

    meldedatum = db.Column(db.Date,default=date.today)

    verfallsdatum = db.Column(db.Date)

    standardtext = db.Column(db.Text)

    campus = db.relationship("Campus",back_populates="fundbueros")


    posts = db.relationship("Post",back_populates="fundbuero")

    posts = db.relationship("Post", back_populates="fundbuero")



class Post(db.Model):

    __tablename__ = "post"

    post_id = db.Column(db.Integer,primary_key=True)

    user_id = db.Column(db.Integer,db.ForeignKey("standardUser.user_id"))

    fundbuero_id = db.Column(db.Integer,db.ForeignKey("fundbuero.fundbuero_id"))

    titel = db.Column(db.String,nullable=False)
    post_id = db.Column(db.Integer, primary_key=True )

    user_id = db.Column(db.Integer,db.ForeignKey("standardUser.user_id") )

    fundbuero_id = db.Column( db.Integer,db.ForeignKey("fundbuero.fundbuero_id"))

    titel = db.Column(db.String,nullable=False )

    meldedatum = db.Column(db.Date)

    verlustdatum = db.Column(db.Date)

    ablaufdatum = db.Column(db.Date)

    schliessdatum = db.Column(db.Date)

    verlustort = db.Column(db.String)

    beschreibung = db.Column(db.Text)

    status = db.Column(db.String,default="laufend")

    views = db.Column(db.Integer,default=0 )

    user = db.relationship("StandardUser",back_populates="posts")

    fundbuero = db.relationship("Fundbuero",back_populates="posts")
    status = db.Column( db.String, default="laufend")

    views = db.Column(db.Integer, default=0 )

    user = db.relationship("StandardUser",back_populates="posts")

    fundbuero = db.relationship( "Fundbuero", back_populates="posts")
   