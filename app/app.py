from flask import Flask
from flask_login import LoginManager

from app.auth.api import AUTH_API
from app.commands import create_tables
from app.config import DATABASE_URI, SECRET_KEY
from app.models import DB, User
from app.todo.api import TODO_API


def create_app():
    app = Flask(__name__)

    # SQLAlchemy configurations.
    app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URI
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

    app.config['SECRET_KEY'] = SECRET_KEY

    # Flask login-manager to manage user login.
    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = 'auth-api.login'
 
    register_blueprint(app)
    initiate_db(app)

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(user_id)
    
    app.cli.add_command(create_tables)

    return app


def initiate_db(app):
    DB.init_app(app=app)


def register_blueprint(app):
    app.register_blueprint(TODO_API)
    app.register_blueprint(AUTH_API)
