import dj_database_url
from kamoorcorner.settings import *

DEBUG=False
TEMPLATE_DEBUG=DEBUG

ALLOWED_HOSTS=[
    'localhost',
    '.herokuapp.com',
    '.kamoorkorner.com',
]

SECRET_KEY = get_env_variable("SECRET_KEY")
EMAIL_HOST_USER = get_env_variable("squadran2003")
EMAIL_HOST_PASSWORD = get_env_variable("innocent23")

db_from_env = dj_database_url.config()
DATABASES['default'].update(db_from_env)
