from django.contrib import admin
from .models import Product
from django_summernote.admin import SummernoteModelAdmin
# Register your models here.
@admin.register(Product)
class ProductAdmin(SummernoteModelAdmin):
    list_display = ['name','price',]
    list_filter = ['price','created_at']


