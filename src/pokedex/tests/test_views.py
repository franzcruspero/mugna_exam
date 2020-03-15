from django.test import TestCase, Client
from django.urls import reverse
from pokedex.models import *
import json

class TestViews(TestCase):
    def setUp(self):
        self.client = Client()
        self.pokemon_list_url = reverse('pokemon_list')
        self.pokemon_detail_url = reverse('pokemon_detail', args=['bulbasaur'])
        self.pokemon_create_url = reverse('pokemon_create')
        self.pokemon_delete_url = reverse('pokemon_delete', args=['ivysaur'])
        self.fly_ability = Ability.objects.create(
            name="fly"
        )
        self.grass_type = Type.objects.create(
            name="grass"
        )
        self.bulbasaur = Pokemon.objects.create(
            pokedex_id = 1,
            name="bulbasaur",
            slug="bulbasaur",
            evolution_id=1,
            evolution_order=1
        )

    def test_pokemon_list_GET(self):
        response = self.client.get(self.pokemon_list_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'pokedex/pokemon_list.html')

    def test_pokemon_detail_GET(self):
        response = self.client.get(self.pokemon_detail_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'pokedex/pokemon_detail.html')

    def test_pokemon_create_POST(self):
        url = reverse('pokemon_create')
        response = self.client.post(url, data={
            "pokedex_id": 3,
            "name": "venosaur",
            "slug": "venosaur",
            "evolution_id": 100,
            "evolution_order": 1,
            "types": ['2'],
            "abilities": ['2']
        })

        venosaur = Pokemon.objects.all().last()

        self.assertEquals(response.status_code, 302)
        self.assertEquals(venosaur.name, 'venosaur')
    
    def test_pokemon_delete_DELETE(self):
        ivysaur = Pokemon.objects.create(
            pokedex_id=2,
            name="ivysaur",
            slug="ivysaur"
        )
        ivysaur.types.add(self.grass_type)
        ivysaur.abilities.add(self.fly_ability)


        response = self.client.get(self.pokemon_delete_url)
        self.assertContains(response, 'Are you sure you want to delete')
        self.assertEquals(response.status_code, 200)
        
        post_response = self.client.post(self.pokemon_delete_url)
        self.assertRedirects(post_response, self.pokemon_list_url, 302)

