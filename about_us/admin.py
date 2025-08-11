from django.contrib import admin
from .models import AboutUs,Employee,Position,OurPartner
from django_summernote.admin import SummernoteModelAdmin
# Register your models here.

@admin.register(AboutUs)
class AboutUsAdmin(SummernoteModelAdmin):
    list_display = ['name','logo','established_at']
    summernote_fields = ['detail',]

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['name','position','employee_type','cell','email']

@admin.register(Position)
class PositionAdmin(admin.ModelAdmin):
    list_display = ['name',]

@admin.register(OurPartner)
class OurPartnerAdmin(admin.ModelAdmin):
    list_display = ['name','url']
