import os

# Project information
PROJECT_PATH = os.path.realpath(os.path.dirname(__file__)+'/../../')
PROJECT_NAME = os.path.basename(PROJECT_PATH)

# Helpers
path = lambda *p: os.path.join(PROJECT_PATH, *p)

# Debug
DEBUG = False
TEMPLATE_DEBUG = DEBUG

# Administration
ADMINS = (
    ('Hersonls', 'hersonls@gmail.com'),
)
MANAGERS = ADMINS

# Site
SITE_ID = 1
SECRET_KEY = r"j*c!wkgy9=&ra@=r%zn_shysr!faxtm-+)057=p$jh5kpzm992"
ALLOWED_HOSTS = ('127.0.0.1', 'in.devitz.com')

# Internationalization
TIME_ZONE = 'America/Araguaina'
LANGUAGE_CODE = 'pt-BR'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Media and Static Files
MEDIA_ROOT = path('media')
MEDIA_URL = '/m/'
STATIC_ROOT = path('static')
STATIC_URL = '/s/'

STATICFILES_DIRS = ()

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

# Middlewares
MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)

# Template context processors
TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.core.context_processors.tz',
#    'django.core.context_processors.request',
    'django.contrib.messages.context_processors.messages',

    'context_processors.site'
)

# Templates
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

TEMPLATE_DIRS = (
    path('templates'),
)

# URLs
ROOT_URLCONF = '%s.urls' % PROJECT_NAME

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = '%s.wsgi.application' % PROJECT_NAME

# Apps
INSTALLED_APPS = (
    # Django Apps
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',

    # Project Apps
    'apps.attendee',

    # Third-party Apps
    'south'
)

# Logging
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

# User
AUTH_USER_MODEL = 'attendee.Attendee'

# Email
DEFAULT_FROM_EMAIL = 'Devitz [nao responda] <no-reply@devitz.com>'