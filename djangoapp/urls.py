from django.contrib import admin
from django.urls import path
from fastapi import FastAPI
from fastapi.middleware.asgi import ASGIMiddleware
from myapp.views import app as fastapi_app  # FastAPI app import from views.py
from myapp.views import app as fastapi_app  # FastAPI app import from views.py

urlpatterns = [
    path('admin/', admin.site.urls),  # Django Admin page
    path('api/', ASGIMiddleware(fastapi_app)),  # FastAPI API route
    path('', ASGIMiddleware(fastapi_app)),  # Root URL pointing to FastAPI
]