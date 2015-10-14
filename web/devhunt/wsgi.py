"""
WSGI config for devhunt project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/howto/deployment/wsgi/
"""
import os
import sys
from os.path import join
from devhunt import settings
from django.core.wsgi import get_wsgi_application


sys.path.insert(0, join(settings.PROJECT_ROOT))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "devhunt.settings")
application = get_wsgi_application()
