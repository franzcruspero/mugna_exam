from django.views.generic.detail import DetailView
from django.views.generic import ListView
from django_filters.views import FilterView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.base import TemplateView

from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render, redirect

from .models import *
from .forms import PokemonForm
from .filters import PokemonFilter

class HomeView(TemplateView):
    template_name = "pokedex/home.html"

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        pokemon = Pokemon.objects.filter(name__in=["Bulbasaur", "Charmander", "Squirtle"])
        context["pokemon"] = pokemon
        print(context)
        return context

class PokemonListView(FilterView):
    model = Pokemon
    paginate_by = 25
    filterset_class = PokemonFilter
    template_name = "pokedex/pokemon_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = PokemonFilter(self.request.GET, queryset=self.get_queryset())
        query = self.request.GET.copy()
        if 'page' in query:
            del query['page']
        context['queries'] = query
        return context


class PokemonDetailView(DetailView):
    model = Pokemon

class PokemonCreateView(CreateView):
    template_name = "pokedex/forms.html"
    form_class = PokemonForm
    # success_message = "%(title)s has been created at %(created_at)s."
    # fields = ["title", "description"]

    def form_valid(self, form, *args, **kwargs):
        # form.instance.last_edited_by = self.request.user
        valid_form = super(PokemonCreateView, self).form_valid(form, *args, **kwargs)
        # messages.success(self.request, "Book created!")
        # send signals
        return valid_form

    # def get_success_url(self):
    #     return redirect('home')

class PokemonUpdateView(UpdateView):
    model = Pokemon
    form_class = PokemonForm
    template_name = "pokedex/forms.html"

class PokemonDeleteView(DeleteView):
    model = Pokemon
    
    # def get_success_url(self):
    #     return reverse("book_list")