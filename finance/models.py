from django.db import models
from django.utils.translation import gettext_lazy as _

from staffs.models import Staff, Ttj
# Create your models here.

class SalaryPayment(models.Model):
    class Meta:
        verbose_name = _("Hodimlarning oylik maoshi to'lovi")
        verbose_name_plural = _("Hodimlarning oylik maoshi to'lovlari")
    staff_id = models.ForeignKey(Staff, on_delete=models.CASCADE, verbose_name=_("Xodim"))
    amount = models.DecimalField(max_digits=15, decimal_places=2, verbose_name=_("miqdor"), help_text=_("UZS da kiritilsin"))
    description = models.TextField(verbose_name=_("Izoh"))
    payed_at = models.DateTimeField(auto_now_add=True, verbose_name=_("To'langan vaqt"))

    def __str__(self):
        return f"{self.staff_id} | {self.amount} UZS"


class KPI(models.Model):
    class Meta:
        verbose_name = _("KPI")
        verbose_name_plural = _("KPI")
    staff_id = models.ForeignKey(Staff, on_delete=models.CASCADE, verbose_name=_("Xodim"))
    amount = models.DecimalField(max_digits=15, decimal_places=2, verbose_name=_("miqdor"), help_text=_("UZS da kiritilsin"))
    description = models.TextField(verbose_name=_("Izoh"), help_text=_("KPI berilish sabablari yoziladi"))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("Tayinlangan vaqt"))

    def __str__(self):
        return f"{self.staff_id} | {self.amount} UZS"


class Penalty(models.Model):
    class Meta:
        verbose_name = _("Jarima")
        verbose_name_plural = _("Jarimalar")
    staff_id = models.ForeignKey(Staff, on_delete=models.CASCADE, verbose_name=_("Xodim"))
    amount = models.DecimalField(max_digits=15, decimal_places=2, verbose_name=_("miqdor"), help_text=_("UZS da kiritilsin"))
    description = models.TextField(verbose_name=_("Izoh"), help_text=_("Jarima berilish sabablari yoziladi"))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("Tayinlangan vaqt"))

    def __str__(self):
        return f"{self.staff_id} | {self.amount} UZS"