from django import forms

from .models import Pokemon

class PokemonForm(forms.ModelForm):
    class Meta:
        model = Pokemon
        fields = [
            "pokedex_id",
            "name",
            "height",
            "weight",
            "description",
            "types",
            "abilities",
            "speed",
            "special_defense",
            "special_attack",
            "defense",
            "attack",
            "hp",
            "image_url",
        ]