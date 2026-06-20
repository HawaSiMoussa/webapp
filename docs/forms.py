from flask_wtf import FlaskForm
from wtforms.fields import StringField, TextAreaField, DateField, SubmitField
from wtforms.validators import InputRequired, Length 
from datetime import date 

#Kontaktformular 1.2
class ContactForm(FlaskForm):
    name = StringField("Name", validators=[InputRequired()])
    username = StringField("Benutzername", validators=[InputRequired()])
    phone_number = StringField("Telefonnummer", validators=[InputRequired()])                     
    submit = SubmitField("Registrieren")

#Post erstellen
class CreatePostForm(FlaskForm):
    title = StringField("Titel", validators=[InputRequired()])
    # begrenzte Anzahl an Zeichen
    description = TextAreaField("Beschreibung",validators=[InputRequired(),Length(max=500)])
    lost_date = DateField("Verlustdatum", validators=[InputRequired()])
    lost_area = StringField("Verlustort", validators=[InputRequired()])
    submit = SubmitField("Veröffentlichen")