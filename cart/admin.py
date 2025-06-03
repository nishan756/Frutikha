from django.contrib import admin
from .models import Cart,CartItem,ConfirmOrder,Coupon
# Register your models here.

@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ['user','created_at']

@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    list_display = ['cart','product','order_status','total_price','created_at']

@admin.register(ConfirmOrder)
class ConfirmOrderAdmin(admin.ModelAdmin):
    list_display = ['cart','name','phone','total_price','discount_price','created_at','order_status']

@admin.register(Coupon)
class CouponAdmin(admin.ModelAdmin):
    list_display = ['code','discount','is_active','created_at']



    
    
