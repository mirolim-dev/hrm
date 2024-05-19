from django.db import models

from staffs.models import Staff, Ttj
# Create your models here.

class SalaryPayment(models.Model):
    class Meta:
        verbose_name = "Hodimlarning oylik maoshi to'lovi"
        verbose_name_plural = "Hodimlarning oylik maoshi to'lovlari"
    staff_id = models.ForeignKey(Staff, on_delete=models.CASCADE, verbose_name="Xodim")
    amount = models.DecimalField(max_digits=15, decimal_places=2, verbose_name="miqdor", help_text="UZS da kiritilsin")
    description = models.TextField(verbose_name="Izoh")
    payed_at = models.DateTimeField(auto_now_add=True, verbose_name="To'langan vaqt")

    def __str__(self):
        return f"{self.staff_id} | {self.amount} UZS"


class KPI(models.Model):
    class Meta:
        verbose_name = "KPI"
        verbose_name_plural = "KPI"
    staff_id = models.ForeignKey(Staff, on_delete=models.CASCADE, verbose_name="Xodim")
    amount = models.DecimalField(max_digits=15, decimal_places=2, verbose_name="miqdor", help_text="UZS da kiritilsin")
    description = models.TextField(verbose_name="Izoh", help_text="KPI berilish sabablari yoziladi")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Tayinlangan vaqt")

    def __str__(self):
        return f"{self.staff_id} | {self.amount} UZS"


class Penalty(models.Model):
    class Meta:
        verbose_name = "Jarima"
        verbose_name_plural = "Jarimalar"
    staff_id = models.ForeignKey(Staff, on_delete=models.CASCADE, verbose_name="Xodim")
    amount = models.DecimalField(max_digits=15, decimal_places=2, verbose_name="miqdor", help_text="UZS da kiritilsin")
    description = models.TextField(verbose_name="Izoh", help_text="Jarima berilish sabablari yoziladi")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Tayinlangan vaqt")

    def __str__(self):
        return f"{self.staff_id} | {self.amount} UZS"