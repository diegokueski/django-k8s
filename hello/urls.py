# pages/urls.py
from django.urls import path
from .views import healthView

urlpatterns = [
    path("", healthView, name="home"),
    path("health/", healthView, name="home"),
]