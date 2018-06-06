from __future__ import unicode_literals

from django.apps import AppConfig


class InceptionsConfig(AppConfig):
    name = 'inceptions'

    def ready(self):
        from . import signals_handler
        super().ready()
