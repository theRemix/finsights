from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("load", views.load, name="load"),
    path("categorize", views.categorize, name="categorize"),
    path("query", views.query, name="query"),
]
