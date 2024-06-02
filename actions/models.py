from django.db import models
from django.utils.translation import gettext_lazy as _


from staffs.models import Staff, Ttj
# Create your models here.

class StaffLeaving(models.Model):
    class Meta:
        verbose_name = _("Ishdan bo'shagan xodim")
        verbose_name_plural = _("Ishdan bo'shagan xodimlar")
    staff_id = models.ForeignKey(Staff, on_delete=models.CASCADE, verbose_name=_('Xodim'))
    reason = models.TextField(verbose_name=_("Sabab"))
    left_at = models.DateTimeField(auto_now_add=True, verbose_name=_("Bo'shatilgan vaqti"))

    def __str__(self):
        return self.staff_id.__str__()


class Attandance(models.Model):
    class Meta:
        verbose_name = _("Davomat")
        verbose_name_plural = _("Davomatlar")
    ttj_id = models.ForeignKey(Ttj, on_delete=models.CASCADE, verbose_name=_("Bino"))
    staff_id = models.ForeignKey(Staff, on_delete=models.CASCADE, verbose_name=_("Xodim"))
    tracked_at = models.DateTimeField(auto_now_add=True, verbose_name=_("Qayd etilgan vaqt"))

    def __str__(self)->str:
        return self.staff_id.__str__() + "|" + self.ttj_id.__str__()


