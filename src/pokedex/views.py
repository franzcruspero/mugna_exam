from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.base import TemplateView

from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render, redirect

from .models import *

class HomeView(TemplateView):
    template_name = "pokedex/home.html"

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        pokemon = Pokemon.objects.filter(name__in=["Bulbasaur", "Charmander"])
        context["pokemon"] = pokemon
        return context

class PokemonListView(ListView):
    model = Pokemon

class PokemonDetailView(DetailView):
    model = Pokemon