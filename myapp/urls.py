from django.urls import path

from . import views

urlpatterns = [
    path("", views.h, name="h"),
]