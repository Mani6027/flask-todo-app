import logging
import os


# Logging 
LOG_FORMAT = '%(asctime)s | %(name)-25s | %(levelname)-7s | %(message)s'
LOG_LEVEL = os.getenv('LOG_LEVEL', 'INFO')
logging.basicConfig(level=LOG_LEVEL, format=LOG_FORMAT)
LOGGER = logging.getLogger(__name__)

# Secretkey
SECRET_KEY = b'_5#y2L"F4Q8z\n\xec]/'

# Databse uri
DATABASE_URI = os.getenv('DATABASE_URL')
