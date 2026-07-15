from flask_wtf import FlaskForm
from wtforms.fields import StringField, TextAreaField, DateField, SubmitField, SelectField, EmailField, PasswordField, BooleanField
from wtforms.validators import InputRequired, Length, ValidationError, Email, Regexp
from datetime import date

# Kontaktformular 1.2
class ContactForm(FlaskForm):
    name = StringField("Name", validators=[InputRequired()])
    username = StringField("Benutzername", validators=[InputRequired()])
    phone_number = StringField("Telefonnummer", validators=[InputRequired()])
    submit = SubmitField("Registrieren")


# Post erstellen
class CreatePostForm(FlaskForm): #FlaskForm geerbt

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

# Login-Formular # ÄNDERE DIESEN TEIL IN DEINER FORMS.PY
class CreateLogin(FlaskForm):
    # Campus entfernt, da beim Login nicht nötig

    campus = SelectField(
        "Campus",
        choices=[("Schöneberg", "Schöneberg"), ("Lichtenberg", "Lichtenberg"), ("Startup Incubator", "Startup Incubator")],
        validators=[InputRequired()]
    )
    hwrmail = EmailField(
        "HWR-Mail",
        validators=[InputRequired(), Email(), Regexp(r'^[a-zA-Z0-9._%+-]+@(hwr-berlin\.de|student\.hwr-berlin\.de|dot\.hwr-berlin\.de)$', message="Bitte geben Sie ihre gültige HWR-Mail-Adresse ein.")]
    )

    passwort = PasswordField(
        "Passwort",
        validators=[InputRequired(), Length(min=8)]
    )

    submit = SubmitField("Login")

# Registrierungsformular
class RegisterForm(FlaskForm):

    campus = SelectField(
        "Campus",
        choices=[("Schöneberg", "Schöneberg"), ("Lichtenberg", "Lichtenberg"), ("Startup Incubator", "Startup Incubator")],
        validators=[InputRequired()]
    )

    hwrmail = EmailField(
        "HWR-Mail",
        validators=[InputRequired(), Email(), Regexp(r'^[a-zA-Z0-9._%+-]+@(hwr-berlin\.de|stud\.hwr-berlin\.de|dot\.hwr-berlin\.de)$', message="Bitte geben Sie ihre gültige HWR-Mail-Adresse ein.")]
    )

    passwort = PasswordField(
        "Passwort",
        validators=[InputRequired(), Length(min=8)]
    )

    benachrichtigung = BooleanField(
        "Benachrichtigung erlauben"
    )

    submit = SubmitField("Registrieren")
    
    # Suchleiste
class Suchleiste(FlaskForm):
  suchfeld = StringField( "Suchbegriff", 
       validators=[InputRequired()]
  )
  
  submit = SubmitField("Suchen")

# Edit Profile Form
class EditProfileForm(FlaskForm):
    
    benutzername = StringField( "Benutzername", validators=[InputRequired()])

    name = StringField(
        "Name",
        validators=[InputRequired()]
    )

    telefonnummer = StringField(
        "Telefonnummer"
    )

    campus_id = SelectField(
        "Campus",
        choices=[
            ("Schöneberg", "Schöneberg"),
            ("Lichtenberg", "Lichtenberg"),
            ("Startup Incubator", "Startup Incubator")
        ]
    )

    submit = SubmitField("Änderungen speichern")