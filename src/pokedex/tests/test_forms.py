from django.test import TestCase
from pokedex.forms import *
from pokedex.models import *

class TestForms(TestCase):
    def test_pokemon_form_valid_data(self):
        Type.objects.create(name="fly")
        Ability.objects.create(name="Fat Hand")
        form = PokemonForm(data={
            'name': 'test',
            'types': ['1'],
            'abilities': ['1']
        })

        self.assertTrue(form.is_valid())

    def test_pokemon_form_not_valid_data(self):
        form = PokemonForm(data={})

        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 3)