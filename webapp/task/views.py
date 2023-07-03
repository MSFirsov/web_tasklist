from flask import Blueprint, flash, current_app, render_template, redirect, request, url_for
from flask_login import current_user
from webapp.task.forms import CreateTaskForm
from webapp.task.models import Task
from webapp.db import db


blueprint = Blueprint('task', __name__)


@blueprint.route('/')
def index():
    title = 'Главная'
    # task_list = Task.query.filter_by(user_id=current_user.id).all()
    task_list = Task.query.filter_by().all()
    return render_template('task/index.html', page_title=title, task_list=task_list)


@blueprint.route('/create_task/<date_id>')
def create_task(date_id):

    title = 'Создание задачи'
    task_form = CreateTaskForm(date_id=date_id)
    return render_template('task/create_task.html', page_title=title, task_form=task_form)


@blueprint.route('/process-create', methods=['POST'])
def process_create():
    form = CreateTaskForm()
    if form.validate_on_submit():
        task = Task(text=form.task_text.data, date_id=form.date_id.data, user_id=current_user.id)
        db.session.add(task)
        db.session.commit()
        flash('added comlete')
    else:
        for field, errors in form.errors.items():
            for error in errors:
                flash('Ошибка в заполнении поля "{}": - {}'.format(
                    getattr(form, field).label.text,
                    error
                ))
    return redirect(request.referrer)
