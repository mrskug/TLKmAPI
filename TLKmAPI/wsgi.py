"""
WSGI konfiguration för TLKmAPI projektet.

Den avslöjar en WSGI modulnivå variabel ``application``

För mer information om denna fil se
https://docs.djangoproject.com/en/1.7/howto/deployment/wsgi/
"""

import os, sys

# sökväg för TLKmAPI
sys.path.append('/srv/TLKmAPI/')
os.environ["DJANGO_SETTINGS_MODULE"] = "TLKmAPI.settings"

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
