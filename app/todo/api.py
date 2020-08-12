import logging
from datetime import datetime
from uuid import uuid4

from flask import (Blueprint, jsonify, redirect, render_template, request,
                   session, url_for)

from app.models import DB, Todo
from sqlalchemy import asc, desc
from sqlalchemy.exc import IntegrityError


TODO_API = Blueprint(name='todo-api', import_name=__name__, url_prefix='/todo')
LOGGER = logging.info(__name__)


@TODO_API.route('/health', methods=['GET'])
def health():
    return jsonify({'status': 'success',
                    'app-status': 'healthy'}), 200


@TODO_API.route('/create', methods=['POST'])
def create_task():
    task_name = request.form['task_name']
    task = Todo(id=uuid4(),
                task_name=task_name,
                email=session['email'],
                status='not-completed')
    DB.session.add(task)
    DB.session.commit()
    return redirect(url_for('todo-api.task_view'))


@TODO_API.route('/update/<string:id>')
def update_task(id):
    task = Todo.query.get(id)
    task.status = 'completed'
    task.updated_at = datetime.now()
    DB.session.commit()
    return redirect(url_for('todo-api.task_view'))


@TODO_API.route('/delete/<string:id>')
def delete_task(id):
    task = Todo.query.get(id)
    DB.session.delete(task)
    DB.session.commit()
    return redirect(url_for('todo-api.task_view'))


@TODO_API.route('/reopen/<string:id>')
def reopen_task(id):
    task = Todo.query.get(id)
    task.status = 'not-completed'
    task.updated_at = datetime.now()
    DB.session.commit()
    return redirect(url_for('todo-api.task_view'))


@TODO_API.route('/task', methods=['POST', 'GET'])
def task_view():
    if request.method == 'POST':
        session['email'] = request.form.get('email')
        email = request.form.get('email')
    elif request.method == 'GET':
        email = session['email']
    tasks = Todo.query.filter(Todo.email == email).order_by(desc(Todo.created_at)) .all()
    return render_template('tasks.html', todo_list=tasks)
