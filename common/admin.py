from django.contrib import admin
from .models import Currency,ShipmentCharge
# Register your models here.

@admin.register(Currency)
class CurrencyAdmin(admin.ModelAdmin):
    list_display = ['name',]

@admin.register(ShipmentCharge)
class ChargeAdmin(admin.ModelAdmin):
    list_display = ['location','inner_charge','outer_charge']
    
