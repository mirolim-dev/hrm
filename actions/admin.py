from django.contrib import admin

from .models import StaffLeaving, Attandance
from .custom_filters import FilterAttandanceByTime
# Register your models here.

class StaffLeavingAdmin(admin.ModelAdmin):
    list_display = ['id', 'staff_id', 'left_at']
    search_fields = ['staff_id__first_name', 'staff_id__last_name', 'staff_id__ttj_id__name']
    list_filter = ['staff_id__ttj_id', 'staff_id__gender', 'staff_id__role']
admin.site.register(StaffLeaving, StaffLeavingAdmin)


class AttandanceAdmin(admin.ModelAdmin):
    list_display = ['id', 'ttj_id', 'staff_id', 'tracked_at']
    search_fields = ['ttj_id__name', 'staff_id__first_name', 'staff_id__last_name']
    list_filter = ['ttj_id', 'staff_id__role', FilterAttandanceByTime]
admin.site.register(Attandance, AttandanceAdmin)