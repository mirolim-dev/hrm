from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver

from .models import StaffLeaving

@receiver(post_save, sender=StaffLeaving)
def update_staff_is_working_status(sender, instance, **kwargs):
    staff = instance.staff_id
    staff.is_working = False
    staff.save()
