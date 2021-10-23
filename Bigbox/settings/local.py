"""Development settings."""

from .base import *  # NOQA
from .base import env

# Base

DEBUG = True

# Security

SECRET_KEY = env('DJANGO_SECRET_KEY', default='%k@1qk(6a6f0q&(8z01m%bck5o+5bs9j5td)4(37n4pm-gon72')

# Cache

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        'LOCATION': ''
    }
}

# Templates

TEMPLATES[0]['OPTIONS']['debug'] = DEBUG  # NOQA

# Email

EMAIL_BACKEND = env('DJANGO_EMAIL_BACKEND', default='django.core.mail.backends.console.EmailBackend')
EMAIL_HOST = 'localhost'
EMAIL_PORT = 1025

# django-extensions

INSTALLED_APPS += ['django_extensions']  # noqa F405
