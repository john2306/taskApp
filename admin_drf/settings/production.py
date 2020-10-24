from .base import *

DEBUG = False


ALLOWED_HOSTS = ['165.227.12.179','taskapp.ml','www.taskapp.ml','*.taskapp.ml']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'dreamdb',
        'USER': 'dream_admin',
        'PASSWORD': 'qazwsx,.-UNI',
        'HOST': 'localhost',
        'PORT': '',
    }
}

STATICFILES_DIRS = (BASE_DIR, 'static')
