# Flask-Todo-App

Simple ToDo application using python-flask

## Development
Install all package requirements in a virtualenv with

```bash
pipenv install
```

## Environment Variables

Create a .env file with the following environment variables.

```ini
FLASK_APP=run.py
FLASK_ENV=development
FLASK_RUN_PORT=5008
FLASK_DEBUG=1
LOG_LEVEL=DEBUG

# Database
DATABASE_USERNAME=postgres
DATABASE_PASSWORD=postgres
DATABASE_HOST=localhost
DATABASE_NAME=postgres
DATABASE_PORT=5432

```

### Serve with Flask

Start a local Flask server with the following command

```bash
flask run
```

