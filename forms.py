from flask_wtf import FlaskForm
from wtforms.fields import SelectField, EmailField, PasswordField, BooleanField, SubmitField,StringField
from wtforms.validators import InputRequired, Email, Length, Regexp

class CreateLogin(FlaskForm):


  campus = SelectField(
  "Campus",
  choices=[("Schöneberg","Schöneberg"),("Lichtenberg","Lichtenberg")],
  validators=[InputRequired()]
 )

  hwrmail = EmailField(
  "Hwr-Mail",
  validators= [InputRequired(),Email(),
               ]
)

  passwort = PasswordField(
  "passwort", 
  validators=[InputRequired(), Length(min=8)]
 )

  benachrichtigung = BooleanField("Hwr-Mail Benachrichtigungen erlauben", 
)
submit = SubmitField("Login")

class Suchleiste(FlaskForm):
  suchbegriff = StringField( "Suchbegriff", 
       validators=[InputRequired()]
  )
  
  submit = SubmitField("Suchen")


