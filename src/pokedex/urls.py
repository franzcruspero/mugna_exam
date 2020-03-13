from django.contrib import admin
from django.urls import path

from django.contrib.auth import views as auth_views

from .views import (
    HomeView, PokemonCreateView, PokemonDetailView, PokemonListView, PokemonUpdateView,
    PokemonDeleteView,
)

urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('pokemon/', PokemonListView.as_view(), name="pokemon_list"),
    path('pokemon-new/', PokemonCreateView.as_view(), name="pokemon_create"),
    path('pokemon/<slug:slug>/', PokemonDetailView.as_view(), name="pokemon_detail"),
    path('pokemon/<slug:slug>/update', PokemonUpdateView.as_view(), name="pokemon_update"),
    path('pokemon/<slug:slug>/delete', PokemonDeleteView.as_view(), name="pokemon_delete"),
]
