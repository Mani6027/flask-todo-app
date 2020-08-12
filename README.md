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
FLASK_RUN_PORT=5000
FLASK_DEBUG=1
LOG_LEVEL=DEBUG

# Database
DATABASE_URL=postgresql+psycopg2://postgres:postgres@localhost:5432/postgres

```

### Serve with Flask

Start a local Flask server with the following command

```bash
flask run
```

