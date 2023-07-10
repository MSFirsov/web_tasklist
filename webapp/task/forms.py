from flask_wtf import FlaskForm
from wtforms import HiddenField, SubmitField, StringField
from wtforms.validators import DataRequired


class CreateTaskForm(FlaskForm):
    num_week_day = HiddenField('num_week_day', validators=[DataRequired()])
    task_text = StringField(validators=[DataRequired()],
                            render_kw={'class': 'form-control', 'placeholder': 'Введите текс задания'})
    submit = SubmitField('Создать!', render_kw={'class': 'btn btn-outline-secondary'})
