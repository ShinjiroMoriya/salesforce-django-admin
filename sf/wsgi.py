"""
WSGI config for sf project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
from whitenoise.django import DjangoWhiteNoise
from wsgi_basic_auth import BasicAuth

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "sf.settings")

application = DjangoWhiteNoise(get_wsgi_application())

application = BasicAuth(application)
