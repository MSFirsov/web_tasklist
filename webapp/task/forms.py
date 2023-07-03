from flask_wtf import FlaskForm
from wtforms import HiddenField, SubmitField, StringField
from wtforms.validators import DataRequired


class CreateTaskForm(FlaskForm):
    date_id = HiddenField('ID дня', validators=[DataRequired()])
    task_text = StringField('Текст задание', validators=[DataRequired()],
                            render_kw={'class': 'form-control', 'placeholder': 'Input task'})
    submit = SubmitField('Создать!', render_kw={'class': 'btn btn-outline-secondary'})
