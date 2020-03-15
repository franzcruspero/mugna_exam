from django.db.models.signals import pre_save
from django.utils.text import slugify

from .models import Pokemon

def pre_save_pokemon(sender, instance, *args, **kwargs):
    slug = slugify(instance.name)
    instance.slug = slug

pre_save.connect(pre_save_pokemon, sender=Pokemon)