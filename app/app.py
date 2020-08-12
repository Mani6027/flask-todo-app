from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

from app.auth.api import AUTH_API
from app.config import (COGNITO_APP_CLIENT_ID, COGNITO_APP_CLIENT_SECRET,
                        COGNITO_USER_POOL_ID, DATABASE_URI)
from app.models import DB, User
from app.todo.api import TODO_API


def create_app():
    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URI
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
    app.config['COGNITO_USER_POOL_ID'] = COGNITO_USER_POOL_ID
    app.config['COGNITO_APP_CLIENT_ID'] = COGNITO_APP_CLIENT_ID
    app.config['COGNITO_APP_CLIENT_SECRET'] = COGNITO_APP_CLIENT_SECRET
    
    app.config['SECRET_KEY'] = b'_5#y2L"F4Q8z\n\xec]/'

    login_manager = LoginManager()
    login_manager.login_view = 'auth-api.login'
    login_manager.init_app(app)
 
    register_blueprint(app)
    initiate_db(app)

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(user_id)

    return app


def initiate_db(app):
    DB.init_app(app=app)


def register_blueprint(app):
    app.register_blueprint(TODO_API)
    app.register_blueprint(AUTH_API)
