from django.views.generic.detail import DetailView
import pdb
from django.views.generic import ListView
from django_filters.views import FilterView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.base import TemplateView

from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render, redirect
from django.urls import reverse

from .models import *
from .forms import PokemonForm, UpdatePokemonForm
from .filters import PokemonFilter

class HomeView(TemplateView):
    template_name = "pokedex/home.html"

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        pokemon = Pokemon.objects.filter(name__in=["Bulbasaur", "Charmander", "Squirtle"])
        context["pokemon"] = pokemon
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

    def get_context_data(self, **kwargs):
        context = super(PokemonDetailView, self).get_context_data(**kwargs)
        double_damage_list = []
        half_damage_list = []
        no_damage_list = []
        quadruple_damage_list = []
        quarter_damage_list = []

        first_stage = []
        second_stage = []
        third_stage = []

        qs = Pokemon.objects.filter(name=self.object)

        for item in qs:
            before_pokemon = Pokemon.objects.filter(pokedex_id=item.pokedex_id-1)
            after_pokemon = Pokemon.objects.filter(pokedex_id=item.pokedex_id+1)
            qs_type = item.types.all()
            evolution_id = item.evolution_id

        evolution_list = Pokemon.objects.filter(evolution_id=evolution_id)

        for pokemon in evolution_list:
            if pokemon.evolution_order == 1:
                first_stage.append(Pokemon.objects.filter(name=pokemon))
            elif pokemon.evolution_order == 2:
                second_stage.append(Pokemon.objects.filter(name=pokemon))
            else:
                third_stage.append(Pokemon.objects.filter(name=pokemon))

        for item in qs_type:
            double_damage_list += item.double_damage_from.split(',')
            if item.half_damage_from != "":
                half_damage_list += item.half_damage_from.split(',')
            if item.no_damage_from != "":
                no_damage_list += item.no_damage_from.split(',')

        final_dd_list = double_damage_list.copy()
        final_hd_list = half_damage_list.copy()

        #Logic for computing type effectiveness
        for item in double_damage_list:
            if item in half_damage_list or item in no_damage_list:
                final_dd_list.remove(item)
            if final_dd_list.count(item) == 2:
                quadruple_damage_list.append(item)
                final_dd_list.remove(item)

        for item in half_damage_list:
            if item in double_damage_list or item in no_damage_list:
                final_hd_list.remove(item)
            if final_hd_list.count(item) == 2:
                quarter_damage_list.append(item)
                final_hd_list.remove(item)

        for item in quadruple_damage_list:
            if item in final_dd_list:
                final_dd_list.remove(item)

        for item in quarter_damage_list:
            if item in final_hd_list:
                final_hd_list.remove(item)

        context['before_pokemon'] = before_pokemon
        context['after_pokemon'] = after_pokemon
        context['double_damage_list'] = final_dd_list
        context['quadruple_damage_list'] = quadruple_damage_list
        context['half_damage_list'] = final_hd_list
        context['quarter_damage_list'] = quarter_damage_list
        context['no_damage_list'] = no_damage_list
        context['first_stage'] = first_stage
        context['second_stage'] = second_stage
        context['third_stage'] = third_stage

        return context


class PokemonCreateView(SuccessMessageMixin, CreateView):
    template_name = "pokedex/forms.html"
    form_class = PokemonForm
    success_message = "%(name)s has been added to the Pokedex."

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        evolve_pokemon_list = Pokemon.objects.all().filter(evolution_order__lt=3)
        devolve_pokemon_list = Pokemon.objects.all().filter(evolution_order__gt=1)
        context['evolve_pokemon_list'] = evolve_pokemon_list
        context['devolve_pokemon_list'] = devolve_pokemon_list
        context['form_header'] = "Create New Pokemon"
        return context


    def form_valid(self, form, *args, **kwargs):
        pokedex_id = Pokemon.objects.all().latest('pokedex_id').pokedex_id + 1
        next_evolution_id = Pokemon.objects.all().latest('evolution_id').evolution_id + 1

        if self.request.POST.get("evolve_devolve_new") == "new":
            form.instance.evolution_id = next_evolution_id
            form.instance.evolution_order = 1

        elif self.request.POST.get("evolve_devolve_new") == "evolve":
            selected_pokemon = Pokemon.objects.filter(name=self.request.POST.get(
                                'select_pokemon_evolve')).first()
            evolution_id = selected_pokemon.evolution_id
            form.instance.evolution_id = evolution_id
            form.instance.evolution_order = selected_pokemon.evolution_order + 1

        elif self.request.POST.get("evolve_devolve_new") == "devolve":
            selected_pokemon = Pokemon.objects.filter(name=self.request.POST.get(
                                'select_pokemon_devolve')).first()
            evolution_id = selected_pokemon.evolution_id
            form.instance.evolution_id = evolution_id
            form.instance.evolution_order = selected_pokemon.evolution_order - 1

        form.instance.pokedex_id = pokedex_id
        valid_form = super(PokemonCreateView, self).form_valid(form, *args, **kwargs)
        return valid_form

class PokemonUpdateView(SuccessMessageMixin, UpdateView):
    model = Pokemon
    form_class = UpdatePokemonForm
    template_name = "pokedex/forms.html"
    success_message = "%(name)s has been updated."

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        evolve_pokemon_list = Pokemon.objects.all().filter(evolution_order__lt=3)
        devolve_pokemon_list = Pokemon.objects.all().filter(evolution_order__gt=1)
        qs = Pokemon.objects.filter(name=self.object)
        evolution_order = qs.first().evolution_order
        devolution_pokemon = Pokemon.objects.all().filter(evolution_id=qs.first().evolution_id,
                            evolution_order = evolution_order-1).first()
        
        image_url = qs.first().image_url

        if devolution_pokemon is None:
            devolution_pokemon = context['object']

        context['form_header'] = "Edit Pokemon"
        context['evolve_pokemon_list'] = evolve_pokemon_list
        context['devolve_pokemon_list'] = devolve_pokemon_list
        context['evolution_order'] = evolution_order
        context['image_url'] = image_url
        context['default_pokemon'] = devolution_pokemon

        return context

    def form_valid(self, form, *args, **kwargs):
        if self.request.POST.get("evolve_devolve_new") == "evolve":
            selected_pokemon = Pokemon.objects.filter(name=self.request.POST.get(
                                'select_pokemon_evolve')).first()
            evolution_id = selected_pokemon.evolution_id
            form.instance.evolution_id = evolution_id
            form.instance.evolution_order = selected_pokemon.evolution_order + 1

        elif self.request.POST.get("evolve_devolve_new") == "devolve":
            selected_pokemon = Pokemon.objects.filter(name=self.request.POST.get(
                                'select_pokemon_devolve')).first()
            evolution_id = selected_pokemon.evolution_id
            form.instance.evolution_id = evolution_id
            form.instance.evolution_order = selected_pokemon.evolution_order - 1

        valid_form = super(PokemonUpdateView, self).form_valid(form, *args, **kwargs)
        return valid_form

class PokemonDeleteView(SuccessMessageMixin, DeleteView):
    model = Pokemon
    success_message = "%(name)s has been deleted from the Pokedex."
    
    def get_success_url(self):
        return reverse("pokemon_list")