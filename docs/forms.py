from flask_wtf import FlaskForm
from wtforms.fields import SelectField, EmailField, PasswordField, BooleanField, SubmitField
from wtforms.validators import InputRequired, Email, Regexp, Length

class CreateLogin(FlaskForm):
 campus = SelectField("Campus",choices=[("Schöneberg","Schöneberg"),("Lichtenberg","Lichtenberg")], validators=[InputRequired()])

HWRmail = EmailField("Hwr-Mail", validators=[InputRequired(),Email(), Regexp("@hwr-berlin.de")])
passwort = PasswordField("passwort", validators=[InputRequired(), Length(min=8)])

benachrichtigung = BooleanField("Hwr-Mail Benachrichtigungen erlauben", )







submit = SubmitField('Login')
