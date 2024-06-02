from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _

class ActionsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'actions'
    verbose_name = _('Hodisalar')
    def ready(self) -> None:
        super().ready()
        from actions import signals
