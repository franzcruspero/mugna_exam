from django.contrib import admin
from django import forms
from .models import *

class PokemonAdmin(admin.ModelAdmin):
    exclude = (
        'slug',
    )
    list_display = (
        'pokedex_id',
        'name',
        'description'
    )
    list_display_links = (
        'pokedex_id',
        'name'
    )
    list_filter = (
        'types',
    )
    search_fields = (
        'name',
        '=pokedex_id'
    )
    formfield_overrides = {
        models.ManyToManyField: {'widget': forms.CheckboxSelectMultiple},
}

class TypeAdmin(admin.ModelAdmin):
    search_fields = (
        'name',
    )
    formfield_overrides = {
        models.ManyToManyField: {'widget': forms.CheckboxSelectMultiple},
}

class AbilityAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'description',
    )
    search_fields = (
        'name',
    )
    formfield_overrides = {
        models.ManyToManyField: {'widget': forms.CheckboxSelectMultiple},
}

admin.site.register(Pokemon, PokemonAdmin)
admin.site.register(Ability, AbilityAdmin)
admin.site.register(Type, TypeAdmin)
