from .base import *


ALLOWED_HOSTS = ['127.0.0.1', 'localhost']


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'OPTIONS': {
            'read_default_file': '../store_db.cnf',
        }
    }
}

