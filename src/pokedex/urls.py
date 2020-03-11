from django.contrib import admin
from django.urls import path

from django.contrib.auth import views as auth_views

from .views import *

urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('pokemon/<slug:slug>/', PokemonDetailView.as_view(), name="pokemon_detail"),
    path('pokemon/create/', PokemonCreateView.as_view(), name="pokemon_create"),
]
