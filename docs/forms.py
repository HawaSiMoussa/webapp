from flask_wtf import FlaskForm
from wtforms.fields import StringField, TextAreaField, DateField, SubmitField
from wtforms.validators import InputRequired, Length  

#Post erstellen
class PostForm(FlaskForm):
    title = StringField("Titel")(validators=[InputRequired()])
    description = TextAreaField("Beschreibung")(validators=[InputRequired()])
    lost_date = DateField("Verlustdatum")(validators=[InputRequired()])
    lost_area = StringField("Verlustort")(validators=[InputRequired()])
    submit = SubmitField("Veröffentlichen")