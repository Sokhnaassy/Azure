"""
WSGI config for appli_crypt project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

settings_module='appli_crypt.deployment' if 'WEBSITE_HOST' in os.environ else 'appli_crypt.settings'
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings_module')

application = get_wsgi_application()
