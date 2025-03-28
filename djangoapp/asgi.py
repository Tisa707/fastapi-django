
"""
ASGI config for djangoapp project.
"""

import os
import django
from django.core.asgi import get_asgi_application
from fastapi import FastAPI

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "djangoapp.settings")
django.setup()  # Initialize Django before importing models

from myapp.views import router

django_app = get_asgi_application()

# Create FastAPI app and include router
fastapi_app = FastAPI()
fastapi_app.include_router(router)

# Mount Django app at /django and FastAPI at /
application = FastAPI()
application.mount("/django", django_app)
application.mount("/", fastapi_app)
