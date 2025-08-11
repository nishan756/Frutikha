from django.contrib import admin
from .models import Contact,Feedback,Subscribe

# Register your models here.

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['name','subject','phone','email','created_at']
    list_filter  = ['created_at','email','phone']

@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ['name','occupation']

@admin.register(Subscribe)
class SubscribeAdmin(admin.ModelAdmin):
    list_display = ['email','created_at']
