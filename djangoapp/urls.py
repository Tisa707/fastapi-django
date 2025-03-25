from django.contrib import admin
from django.urls import path
from fastapi import FastAPI
from fastapi.middleware.wsgi import WSGIMiddleware
from myapp.views import app as fastapi_app  # Assuming the FastAPI app is defined in api/views.py

urlpatterns = [
    path('admin/', admin.site.urls),  # Django Admin page
    path('api/', WSGIMiddleware(fastapi_app)),  # FastAPI API
    path('', WSGIMiddleware(fastapi_app)),  # Root URL pointing to FastAPI
]
