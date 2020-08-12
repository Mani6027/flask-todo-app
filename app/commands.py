import click
from flask.cli import with_appcontext

from app.models import DB, User, Todo

@click.command(name='create_tables')
@with_appcontext
def create_tables():
    click.echo('Creating all the tables...')
    DB.create_all()