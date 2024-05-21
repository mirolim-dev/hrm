from django.db import models


from staffs.models import Staff, Ttj
# Create your models here.

class StaffLeaving(models.Model):
    class Meta:
        verbose_name = "Ishdan bo'shagan xodim"
        verbose_name_plural = "Ishdan bo'shagan xodimlar"
    staff_id = models.ForeignKey(Staff, on_delete=models.CASCADE, verbose_name='Xodim')
    reason = models.TextField(verbose_name="Sabab")
    left_at = models.DateTimeField(auto_now_add=True, verbose_name="Bo'shatilgan vaqti")

    def __str__(self):
        return self.staff_id.__str__()


class Attandance(models.Model):
    class Meta:
        verbose_name = "Davomat"
        verbose_name_plural = "Davomatlar"
    ttj_id = models.ForeignKey(Ttj, on_delete=models.CASCADE, verbose_name="TTJ")
    staff_id = models.ForeignKey(Staff, on_delete=models.CASCADE, verbose_name="Xodim")
    tracked_at = models.DateTimeField(auto_now_add=True, verbose_name="Qayd etilgan vaqt")

    def __str__(self)->str:
        return self.staff_id.__str__() + "|" + self.ttj_id.__str__()


