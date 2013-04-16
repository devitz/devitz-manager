from .base import *

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ALLOWED_HOSTS = ('127.0.0.1', )

# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': path('database.db'),
    }
}

EMAIL_BACKEND = 'mail_backends.SSLEmailBackend'
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.zoho.com'
EMAIL_HOST_USER = 'no-reply@devitz.com'
EMAIL_HOST_PASSWORD = '2013devitz'
EMAIL_PORT = 465
SERVER_EMAIL = 'no-reply@devitz.com'

LANGUAGE_CODE = 'pt-br'
