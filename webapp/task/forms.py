from flask_wtf import FlaskForm
from wtforms import HiddenField, SubmitField, StringField
from wtforms.validators import DataRequired


class CreateTaskForm(FlaskForm):
    task_date = HiddenField(validators=[DataRequired()])
    task_text = StringField(validators=[DataRequired()],
                            render_kw={'class': 'form-control', 'placeholder': 'Введите текст задания'})
    submit = SubmitField('Создать!', render_kw={'class': 'btn btn-outline-secondary'})
