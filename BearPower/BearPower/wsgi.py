"""
WSGI config for BearPower project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/wsgi/
"""
import sys, traceback

def show_traceback(exc_type, exc_value, tb):
    traceback.print_exception(exc_type, exc_value, tb)
    sys.__excepthook__(exc_type, exc_value, tb)

sys.excepthook = show_traceback

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'BearPower.settings')

application = get_wsgi_application()
