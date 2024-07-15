from django.urls import path
from .api import app
from . import views


urlpatterns = [path("", views.index, name="index"), path("api/", app.urls)]
