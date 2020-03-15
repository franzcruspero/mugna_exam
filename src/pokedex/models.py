from django.db import models
from django.urls import reverse

class Type(models.Model):
    TYPES = (
        ("normal", "Normal"), ("fighting", "Fighting"), ("flying", "Flying"),
        ("poison", "Poison"), ("ground", "Ground"), ("rock", "Rock"), ("bug", "Bug"),
        ("ghost", "Ghost"), ("steel", "Steel"), ("fire", "Fire"), ("water", "Water"),
        ("grass", "Grass"), ("electric", "Electric"), ("psychic", "Psychic"), ("ice", "Ice"),
        ("dragon", "Dragon"), ("dark", "Dark"), ("fairy", "Fairy")
    )
    name = models.CharField(max_length=100, unique=True, null=True)
    double_damage_from = models.CharField(max_length=100, null=True)
    half_damage_from = models.CharField(max_length=100, null=True)
    no_damage_from = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ["name"]

class Ability(models.Model):
    name = models.CharField(max_length=100, unique=True, null=True)
    description = models.TextField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["name"]

class Pokemon(models.Model):
    pokedex_id = models.IntegerField(null=True, unique=True)
    name = models.CharField(max_length=100, unique=True)
    height = models.FloatField(null=True, blank=True, default=1)
    weight = models.FloatField(null=True, blank=True, default=1)
    description = models.TextField(max_length=300, null=True, blank=True)
    types = models.ManyToManyField(Type)
    abilities = models.ManyToManyField(Ability)
    evolution_id = models.IntegerField(null=True)
    evolution_order = models.IntegerField(null=True)
    speed = models.IntegerField(null=True, blank=True, default=1)
    special_defense = models.IntegerField(null=True, blank=True, default=1)
    special_attack = models.IntegerField(null=True, blank=True, default=1)
    defense = models.IntegerField(null=True, blank=True, default=1)
    attack = models.IntegerField(null=True, blank=True, default=1)
    hp = models.IntegerField(null=True, blank=True, default=1)
    image_url = models.CharField(max_length=100, default="https://tinyurl.com/yx6v48ln",
                                 null=True, blank=True)
    slug = models.SlugField(null=True)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("pokemon_detail", kwargs={"slug": self.slug})

    class Meta:
        ordering = ["pokedex_id"]
