from .base import *

DEBUG = False


ALLOWED_HOSTS = ['ianalytics.ml','www.ianalytics.com','159.89.48.214']

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
