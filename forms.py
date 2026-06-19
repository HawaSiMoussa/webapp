from flask_wtf import FlaskForm
from wtforms.fields import StringField, SubmitField
from wtforms.validators import InputRequired, Length

class CreateTodoForm(FlaskForm):  # (1.) class CreateTodoForm inherits from FlaskForm.
    description = StringField(validators=[InputRequired(), Length(min=5)])  # (2.) individual form field + validators: not empty, at least 5 characters
    submit = SubmitField('Create') #individual form field
