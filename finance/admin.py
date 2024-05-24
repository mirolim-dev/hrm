from django.contrib import admin

from .models import SalaryPayment, KPI, Penalty
# Register your models here.

class SalaryPaymentAdmin(admin.ModelAdmin):
    list_display = ['staff_id', 'get_ttj_id', 'get_role', 'get_salary', 'amount', 'payed_at']
    search_fields = ['staff_id__first_name', 'staff_id__last_name', 'staff_id__phone']
    list_filter = ['staff_id__role', 'staff_id__ttj_id', 'staff_id__is_working']

    def get_ttj_id(self, obj):
        return obj.staff_id.ttj_id
    get_ttj_id.short_description = 'TTJ'

    def get_role(self, obj):
        return obj.staff_id.get_role_display()
    get_role.short_description = 'Role'

    def get_salary(self, obj):
        return obj.staff_id.salary
    get_salary.short_description = 'Maosh'
admin.site.register(SalaryPayment, SalaryPaymentAdmin)


class KPIAdmin(admin.ModelAdmin):
    list_display = ['staff_id', 'get_ttj_id', 'get_role', 'get_salary', 'amount', 'created_at']
    search_fields = ['staff_id__first_name', 'staff_id__last_name', 'staff_id__phone']
    list_filter = ['staff_id__role', 'staff_id__ttj_id', 'staff_id__is_working']

    def get_ttj_id(self, obj):
        return obj.staff_id.ttj_id
    get_ttj_id.short_description = 'ТЦ'

    def get_role(self, obj):
        return obj.staff_id.get_role_display()
    get_role.short_description = 'Role'

    def get_salary(self, obj):
        return obj.staff_id.salary
    get_salary.short_description = 'Maosh'
admin.site.register(KPI, KPIAdmin)


class PenaltyAdmin(admin.ModelAdmin):
    list_display = ['staff_id', 'get_ttj_id', 'get_role', 'get_salary', 'amount', 'created_at']
    search_fields = ['staff_id__first_name', 'staff_id__last_name', 'staff_id__phone']
    list_filter = ['staff_id__role', 'staff_id__ttj_id', 'staff_id__is_working']

    def get_ttj_id(self, obj):
        return obj.staff_id.ttj_id
    get_ttj_id.short_description = 'ТЦ'

    def get_role(self, obj):
        return obj.staff_id.get_role_display()
    get_role.short_description = 'Role'

    def get_salary(self, obj):
        return obj.staff_id.salary
    get_salary.short_description = 'Maosh'
admin.site.register(Penalty, PenaltyAdmin)