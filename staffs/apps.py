from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _

class StaffsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'staffs'
    verbose_name = _('Xodimlar')