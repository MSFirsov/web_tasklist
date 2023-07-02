from flask import Blueprint, current_app, render_template

from webapp.db import db


blueprint = Blueprint('task', __name__)


@blueprint.route('/')
def index():
    title = 'Главная'
    return render_template('task/index.html', page_title=title)


@blueprint.route('/create_task')
def create_task():
    title = 'Создание задачи'
    return render_template('task/create_task.html', page_title=title)
