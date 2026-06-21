from flask_wtf import FlaskForm

from wtforms.fields import StringField, TextAreaField, DateField, SubmitField
from wtforms.validators import InputRequired, Length, ValidationError
from datetime import date

# Kontaktformular 1.2
class ContactForm(FlaskForm):
    name = StringField("Name", validators=[InputRequired()])
    username = StringField("Benutzername", validators=[InputRequired()])
    phone_number = StringField("Telefonnummer", validators=[InputRequired()])
    submit = SubmitField("Registrieren")


# Post erstellen
class CreatePostForm(FlaskForm):

    title = StringField(
        "Titel",
        validators=[InputRequired()]
    )

    description = TextAreaField(
        "Beschreibung",
        validators=[
            InputRequired(),
            Length(max=500)
        ]
    )

    lost_date = DateField(
        "Verlustdatum",
        validators=[InputRequired()]
    )

    lost_area = StringField(
        "Verlustort",
        validators=[InputRequired()]
    )

    submit = SubmitField("Veröffentlichen")

    # Verlustdatum darf nicht in der Zukunft liegen
    def validate_lost_date(self, field):
        if field.data > date.today():
            raise ValidationError(
                "Verlustdatum darf nicht in der Zukunft liegen."
            )
from wtforms.fields import SelectField, EmailField, PasswordField, BooleanField, SubmitField,StringField
from wtforms.validators import InputRequired, Email, Length, Regexp

class CreateLogin(FlaskForm):

    campus = SelectField(
        "Campus",
        choices=[("Schöneberg", "Schöneberg"), ("Lichtenberg", "Lichtenberg"), ("Startup Incubator", "Startup Incubator")],
        validators=[InputRequired()]
    )

    hwrmail = EmailField(
        "HWR-Mail",
        validators=[InputRequired(), Email()]
    )

    passwort = PasswordField(
        "Passwort",
        validators=[InputRequired(), Length(min=8)]
    )

    benachrichtigung = BooleanField(
        "Benachrichtigungen erlauben"
    )

    submit = SubmitField("Login")


class RegisterForm(FlaskForm):

    campus = SelectField(
        "Campus",
        choices=[("Schöneberg", "Schöneberg"), ("Lichtenberg", "Lichtenberg"), ("Startup Incubator", "Startup Incubator")],
        validators=[InputRequired()]
    )

    hwrmail = EmailField(
        "HWR-Mail",
        validators=[InputRequired(), Email()]
    )

    passwort = PasswordField(
        "Passwort",
        validators=[InputRequired(), Length(min=8)]
    )

    benachrichtigung = BooleanField(
        "Benachrichtigung erlauben"
    )

    submit = SubmitField("Registrieren")
    
class Suchleiste(FlaskForm):
  suchbegriff = StringField( "Suchbegriff", 
       validators=[InputRequired()]
  )
  
submit = SubmitField("Suchen")
