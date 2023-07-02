from flask_wtf import FlaskForm
from wtforms import HiddenField, SubmitField, StringField
from wtforms.validators import DataRequired


class CreateTask(FlaskForm):
    text = StringField()
