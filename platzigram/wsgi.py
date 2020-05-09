#ESTE ES EL ARCHIVO USADO EN DEPLOYMENT PARA PRODUCCIÓN, Y ES LA INTERFAZ WSGI CUANDO NUESTRO ARCHIVO
#ESTÁ CORRRIENDO EN PRODUCCIÓN
"""
WSGI config for platzigram project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'platzigram.settings')

application = get_wsgi_application()
