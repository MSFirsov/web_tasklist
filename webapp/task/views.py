from flask import Blueprint, flash, render_template, redirect, request, url_for
from flask_login import current_user
from webapp.task.forms import CreateTaskForm
from webapp.task.models import Task
from webapp.db import db


blueprint = Blueprint('task', __name__)


@blueprint.route('/')
def index():
    title = 'Главная'
    if current_user.is_authenticated:
        task_list = Task.query.filter_by(user_id=current_user.id).all()
        return render_template('task/index.html', page_title=title, task_list=task_list)
    else:
        return render_template('task/index.html', page_title=title)


@blueprint.route('/create_task/<num_week_day>')
def create_task(num_week_day):

    title = 'Создание задания'
    task_form = CreateTaskForm(num_week_day=num_week_day)
    return render_template('task/create_task.html', page_title=title, task_form=task_form)


@blueprint.route('/process-create', methods=['POST'])
def process_create():
    form = CreateTaskForm()
    if form.validate_on_submit():
        task = Task(text=form.task_text.data, num_week_day=form.num_week_day.data, user_id=current_user.id)
        db.session.add(task)
        db.session.commit()
        flash('Задание добавлено')
        return redirect(url_for('task.index'))
    else:
        for field, errors in form.errors.items():
            for error in errors:
                flash(f'Ошибка в заполнении поля "{getattr(form, field).label.text}": - {error}')
    return redirect(request.referrer)


@blueprint.route('/process_delete/<task_id>')
def del_task(task_id):
    task = Task.query.filter_by(id=task_id).one_or_none()
    db.session.delete(task)
    db.session.commit()
    flash('Задание удалено')
    return redirect(url_for('task.index'))



