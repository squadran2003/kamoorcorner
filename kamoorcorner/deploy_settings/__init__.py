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
EMAIL_HOST = get_env_variable('EMAIL_HOST')
EMAIL_HOST_USER = get_env_variable("EMAIL_HOST_USER")
AWS_S3_ACCESS_KEY_ID = get_env_variable("AWS_ID")
AWS_S3_SECRET_ACCESS_KEY = get_env_variable("AWS_PASS")




db_from_env = dj_database_url.config()
DATABASES['default'].update(db_from_env)
