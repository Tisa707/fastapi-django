"""
ASGI config for djangoapp project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/asgi/
"""




import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "djangoapp.settings")

from django.core.asgi import get_asgi_application
from fastapi import FastAPI
from myapp.views import app as fastapi_app

django_app = get_asgi_application()

# Mount Django app at /django and FastAPI at /api
application = FastAPI()
application.mount("/django", django_app)
application.mount("/api", fastapi_app)

