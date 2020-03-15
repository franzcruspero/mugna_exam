import django_filters
from django_filters import DateFilter, CharFilter, ModelChoiceFilter, ModelMultipleChoiceFilter
from django import forms


from .models import *

class PokemonFilter(django_filters.FilterSet):
    name = CharFilter(field_name="name", lookup_expr="icontains", label="Pokemon",
                widget=forms.TextInput(attrs={
                    'placeholder': 'Pokemon Name', 'class': 'form-control'}
                )
            )
    types = ModelChoiceFilter(queryset=Type.objects.all(),
                widget=forms.Select(attrs={
                    'placeholder': 'Pokemon Name', 'class': 'form-control'}
                )
            )
    class Meta:
        model = Pokemon
        fields = ['name', 'types']
