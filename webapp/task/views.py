import datetime

from flask import Blueprint, flash, render_template, redirect, request, url_for
from flask_login import current_user, login_required
from webapp.task.forms import CreateTaskForm
from webapp.task.models import Task
from webapp.db import db


blueprint = Blueprint('task', __name__)


@blueprint.route('/')
def index():
    title = 'Главная'

    iso_date = datetime.date.today().isocalendar()

    day_list = [
        datetime.date.fromisocalendar(iso_date[0], iso_date[1], 1),
        datetime.date.fromisocalendar(iso_date[0], iso_date[1], 2),
        datetime.date.fromisocalendar(iso_date[0], iso_date[1], 3),
        datetime.date.fromisocalendar(iso_date[0], iso_date[1], 4),
        datetime.date.fromisocalendar(iso_date[0], iso_date[1], 5),
        datetime.date.fromisocalendar(iso_date[0], iso_date[1], 6),
        datetime.date.fromisocalendar(iso_date[0], iso_date[1], 7)
        ]

    if current_user.is_authenticated:
        task_list = Task.query.filter_by(user_id=current_user.id).all()
        return render_template('task/index.html', page_title=title, task_list=task_list, day_list=day_list,
                               week_num=iso_date[1])
    else:
        return render_template('task/index.html', page_title=title)


@blueprint.route('/<week_num>')
def index_with_week(week_num):
    title = 'Главная'

    iso_date = datetime.date.today().isocalendar()

    day_list = [
            datetime.date.fromisocalendar(iso_date[0], int(week_num), 1),
            datetime.date.fromisocalendar(iso_date[0], int(week_num), 2),
            datetime.date.fromisocalendar(iso_date[0], int(week_num), 3),
            datetime.date.fromisocalendar(iso_date[0], int(week_num), 4),
            datetime.date.fromisocalendar(iso_date[0], int(week_num), 5),
            datetime.date.fromisocalendar(iso_date[0], int(week_num), 6),
            datetime.date.fromisocalendar(iso_date[0], int(week_num), 7)
            ]

    if current_user.is_authenticated:
        task_list = Task.query.filter_by(user_id=current_user.id).all()
        return render_template('task/index.html', page_title=title,
                               task_list=task_list, day_list=day_list, week_num=int(week_num))


@blueprint.route('/create_task/<task_date>')
@login_required
def create_task(task_date):

    title = 'Создание задания'
    task_form = CreateTaskForm(task_date=task_date)
    return render_template('task/create_task.html', page_title=title, task_form=task_form)


@blueprint.route('/process-create', methods=['POST'])
@login_required
def process_create():
    form = CreateTaskForm()
    if form.validate_on_submit():
        task_date = datetime.datetime.strptime(form.task_date.data, "%Y-%m-%d")
        task = Task(text=form.task_text.data, task_date=task_date, user_id=current_user.id)
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
@login_required
def del_task(task_id):
    task = Task.query.filter_by(id=task_id).one_or_none()
    if task is None:
        flash('Задания не существует')
        return redirect(url_for('task.index'))

    db.session.delete(task)
    db.session.commit()
    flash('Задание удалено')
    return redirect(url_for('task.index'))

