
"""
ASGI config for djangoapp project.
"""

import os
import django
from django.core.asgi import get_asgi_application
from fastapi import FastAPI

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "djangoapp.settings")
django.setup()  # Initialize Django before importing models

from myapp.views import app as fastapi_app

django_app = get_asgi_application()

# Mount Django app at /django and FastAPI at /api
application = FastAPI()
application.mount("/django", django_app)
application.mount("/api", fastapi_app)
