from django.db import models
import uuid
from django.contrib.auth.models import User
from django.utils.timezone import now
from product.models import Product
from django.utils.timezone import now
# Create your models here.

class Coupon(models.Model):
    code = models.CharField(max_length = 10)
    discount = models.PositiveIntegerField(help_text = 'in percentage')
    is_active = models.BooleanField(default = True)
    created_at = models.DateTimeField(default = now)

    def __str__(self):
        return self.code
    class Meta:
        ordering = ['-created_at']
    
    


class Cart(models.Model):
    id = models.UUIDField(primary_key = True, default = uuid.uuid4,editable = False)
    user = models.OneToOneField(User,on_delete = models.CASCADE)
    created_at = models.DateTimeField(default = now)

    def __str__(self):
        return self.user.username
    
class CartItem(models.Model):
    id = models.UUIDField(primary_key = True, default = uuid.uuid4,editable  = False)
    cart = models.ForeignKey(Cart,on_delete = models.CASCADE)
    product = models.ForeignKey(Product,on_delete = models.CASCADE)
    qty = models.PositiveIntegerField(default = 1)
    total_price = models.IntegerField(blank = True,null = True)
    order_status = models.BooleanField(default = False)
    created_at = models.DateTimeField(default = now)

    def __str__(self):
        return f'Order of {self.cart.user} for {self.product.name}'
    
    def save(self,*args,**kwargs):
        self.total_price = self.qty*self.product.price
        super(CartItem, self).save(*args, **kwargs)

class ConfirmOrder(models.Model):
    id = models.UUIDField(primary_key = True,default = uuid.uuid4,editable = False)
    cart = models.ForeignKey(Cart,on_delete = models.CASCADE)
    name = models.CharField(max_length = 200)
    phone = models.CharField(max_length = 15)
    location = models.CharField(max_length = 500)
    products = models.ManyToManyField(CartItem)
    coupon = models.ForeignKey(Coupon,on_delete = models.SET_NULL,blank = True,null = True)
    total_price = models.PositiveIntegerField(default = 0)
    discount_price = models.PositiveIntegerField(blank = True,null = True)
    ORDER_STATUS = [
        ('Accepted','Accepted'),
        ('Packing','Packing'),
        ('On the way','On the way'),
        ('Placed','Placed'),
        ('Cancled','Cancled'),
    ]
    order_status = models.CharField(choices = ORDER_STATUS,default = 'Accepted',max_length = 12)
    created_at = models.DateTimeField(auto_now_add = True)
    placed_at = models.DateTimeField(blank = True,null = True)

    def __str__(self):
        return f'Confirmed order from {self.name}'
    

    def save(self,*args,**kwargs):
        self.total_price = sum (item.total_price for item in self.products.all())
        for item in self.products.all():
            item.order_status = True
            item.save()

        self.total_price = sum(product.total_price for product in self.products.all())
        if self.coupon and self.coupon.is_active == True:
            self.discount_price = self.total_price - (self.total_price*self.coupon.discount)/100

        if self.order_status == 'Placed':
            self.placed_at = now()

        if self.order_status == 'Cancled':
            for product in self.products.all():
                product.order_status = False
                product.save()
                self.objects.delete()
        super(ConfirmOrder,self).save(*args,**kwargs)

    def Id(self):
        id = str(self.id).split('-')
        return id[-1]
    
    class Meta:
        ordering = ['-created_at']

