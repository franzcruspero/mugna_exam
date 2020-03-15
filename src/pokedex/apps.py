from django.apps import AppConfig


class PokedexConfig(AppConfig):
    name = 'pokedex'

    def ready(self):
        import pokedex.signals
