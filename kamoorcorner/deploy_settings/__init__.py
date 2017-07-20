import dj_database_url
from kamoorcorner.settings import *

DEBUG=True
TEMPLATE_DEBUG=DEBUG

ALLOWED_HOSTS=[
    'localhost',
    '.herokuapp.com',
    '.kamoorkorner.com',
]

SECRET_KEY = get_env_variable("SECRET_KEY")
EMAIL_HOST_USER = get_env_variable("EMAIL_HOST_USER")


db_from_env = dj_database_url.config()
DATABASES['default'].update(db_from_env)
