from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="indice"),
    path('<int:numero>', views.detail, name="detalle")
]