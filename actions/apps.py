from django.apps import AppConfig


class ActionsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'actions'
    verbose_name = 'Hodisalar'
    def ready(self) -> None:
        super().ready()
        from actions import signals
