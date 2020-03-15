from django.test import SimpleTestCase
from django.urls import reverse, resolve
from pokedex.views import *


class TestUrls(SimpleTestCase):
    def test_home_url_resolves(self):
        url = reverse('home')
        self.assertEquals(resolve(url).func.view_class, HomeView)
    
    def test_detail_url_resolves(self):
        url = reverse('pokemon_detail', args=['some-slug'])
        self.assertEquals(resolve(url).func.view_class, PokemonDetailView)

    def test_list_url_resolves(self):
        url = reverse('pokemon_list')
        self.assertEquals(resolve(url).func.view_class, PokemonListView)

    def test_create_url_resolves(self):
        url = reverse('pokemon_create')
        self.assertEquals(resolve(url).func.view_class, PokemonCreateView)

    def test_update_url_resolves(self):
        url = reverse('pokemon_update', args=['some-slug'])
        self.assertEquals(resolve(url).func.view_class, PokemonUpdateView)

    def test_delete_url_resolves(self):
        url = reverse('pokemon_delete', args=['some-slug'])
        self.assertEquals(resolve(url).func.view_class, PokemonDeleteView)
