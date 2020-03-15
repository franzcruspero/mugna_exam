from django import forms

from .models import Pokemon

class PokemonForm(forms.ModelForm):
    class Meta:
        model = Pokemon
        fields = "__all__"
        exclude = ["pokedex_id", "evolution_id", "evolution_order", "slug"]

class UpdatePokemonForm(forms.ModelForm):
    class Meta:
        model = Pokemon
        fields = "__all__"
        exclude = ["evolution_id", "evolution_order", "slug"]