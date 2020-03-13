import django_filters
from django_filters import DateFilter, CharFilter, ModelChoiceFilter


from .models import *

class PokemonFilter(django_filters.FilterSet):
    name = CharFilter(field_name="name", lookup_expr="icontains", label="Pokemon")
    types = ModelChoiceFilter(queryset=Type.objects.all())
    class Meta:
        model = Pokemon
        fields = ['name', 'types']
