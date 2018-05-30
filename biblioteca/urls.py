from django.shortcuts import render
from biblioteca.views import *
from django.urls import path, include

# Create your views here.

urlpatterns = [
    path('', GeneroListView.as_view(), name='genero-list'),
    path('genero/<int:pk>', GeneroDetailView.as_view(), name='genero-detail'),
    path('genero/create', GeneroCreate.as_view(), name='genero-create'),
  ]