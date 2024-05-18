from django.contrib import admin

from .models import Staff, Ttj
from .forms import StaffAdminForm

class StaffAdmin(admin.ModelAdmin):
    form = StaffAdminForm
    list_display = ['first_name', 'last_name', 'phone', 'role', 'is_working', 'ttj_id']
    search_fields = ['first_name', 'last_name', 'phone']
    list_filter = ['role', 'is_working', 'ttj_id']

admin.site.register(Staff, StaffAdmin)
admin.site.register(Ttj)