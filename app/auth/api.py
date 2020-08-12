import logging
from datetime import datetime
from functools import wraps
from uuid import uuid4

from flask import (Blueprint, flash, g, jsonify, redirect, render_template,
                   request, session, url_for)
from werkzeug.security import check_password_hash, generate_password_hash

from app.models import DB, Todo, User
from flask_login import login_user
from flask_restful import Api, Resource
from sqlalchemy.exc import IntegrityError

AUTH_API = Blueprint('auth-api', import_name=__name__, url_prefix='')
LOGGER = logging.info(__name__)

@AUTH_API.route('/')
def index_view():
    return render_template('index.html')


@AUTH_API.route('/register')
def signup():
    return render_template('signup.html')


@AUTH_API.route('/login')
def login():
    return render_template('login.html')


@AUTH_API.route('/register', methods=['POST'])
def register_view():
    email = request.form.get('email')
    password = request.form.get('password')

    user = User.query.filter_by(email=email).first()
    if user:
        flash('Email address already exists')
        return redirect(url_for('auth-api.signup'))
    
    new_user = User(email=email,
                    password=generate_password_hash(password, method='sha256'))
    
    # Need exception, to handle IntergrityError.
    DB.session.add(new_user)
    DB.session.commit()

    return redirect(url_for('auth-api.login'))


@AUTH_API.route('/login', methods=['POST'])
def login_view():
    email = request.form.get('email')
    session['email'] = email
    password = request.form.get('password')

    user = User.query.filter_by(email=email).first()

    if not user or not check_password_hash(user.password, password): 
        flash('Please check your login details and try again.')
        return redirect(url_for('auth-api.login'))

    return redirect(url_for('todo-api.task_view'))


@AUTH_API.route('/logout')
def logout():
    return render_template('login.html')
