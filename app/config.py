import logging
import os


# Logging 
LOG_FORMAT = '%(asctime)s | %(name)-25s | %(levelname)-7s | %(message)s'
LOG_LEVEL = os.getenv('LOG_LEVEL', 'INFO')
logging.basicConfig(level=LOG_LEVEL, format=LOG_FORMAT)
LOGGER = logging.getLogger(__name__)


# Database details
DATABASE_HOST = os.getenv('DATABASE_HOST')
DATABASE_NAME = os.getenv('DATABASE_NAME')
DATABASE_USERNAME = os.getenv('DATABASE_USERNAME')
DATABASE_PORT = int(os.getenv('DATABASE_PORT', 5432))
DATABASE_PASSWORD = os.getenv('DATABASE_PASSWORD')
SQLALCHEMY_TRACK_MODIFICATIONS = True


# Secretkey
SECRET_KEY = b'_5#y2L"F4Q8z\n\xec]/'


# Databse uri
DATABASE_URI = f'postgresql+psycopg2://{DATABASE_USERNAME}:' \
               f'{DATABASE_PASSWORD}@{DATABASE_HOST}:{DATABASE_PORT}/{DATABASE_NAME}'
