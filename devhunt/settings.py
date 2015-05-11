# -*- coding: utf-8 -*-
"""
DEVHUNT GENERAL PROJECT SETTINGS
"""
from __future__ import unicode_literals
from django.utils.translation import ugettext_lazy as _
import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# Apps specifics settings
from foro.settings import *


PROJECT_APPS = [
    # Project
    'devhunt',
    # Reusable apps
    'evento',
	'foro',
	'agenda',
]

THIRD_PARTY_APPS = [
	'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_gravatar',
    'djconfig',
    'haystack',
    'pagedown',
    'markdown_deux',
]

INSTALLED_APPS = THIRD_PARTY_APPS + PROJECT_APPS

DEBUG = False

TEMPLATE_DEBUG = False

ALLOWED_HOSTS = ['*']

ROOT_URLCONF = 'devhunt.urls'

WSGI_APPLICATION = 'devhunt.wsgi.application'

TIME_ZONE = 'America/Bogota'

USE_I18N = True

USE_L10N = True

USE_TZ = True

STATIC_URL = '/static/'

MEDIA_URL = '/media/'


LANGUAGES = (
    ('es', _('Spanish')),
)

LANGUAGE_CODE = 'es-co'

TEMPLATE_LOADERS = (
    'django.template.loaders.app_directories.Loader',
    'django.template.loaders.filesystem.Loader',
)


# Use debug, sqlite, staticfiles dirs etc..

try:
    from .local_settings import *
except ImportError:
    pass

# Production database, smtp, roots etc..

try:
    from .production_settings import *
except ImportError:
    pass
