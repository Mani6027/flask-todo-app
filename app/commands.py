import click
from flask.cli import with_appcontext

from app.models import db, User, Todo

@click.command(name='create_tables')
@with_appcontext
def create_tables():
    db.create_all()