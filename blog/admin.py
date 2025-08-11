from django.contrib import admin
from .models import Blog
from django_summernote.admin import SummernoteModelAdmin
# Register your models here.

@admin.register(Blog)
class BlogAdmin(SummernoteModelAdmin):
    list_display = ['title','created_at','updated_at']
    summernote_fields = ['detail',]
