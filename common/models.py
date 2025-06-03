from django.db import models

# Create your models here.

class Currency(models.Model):
    name = models.CharField(max_length = 20)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = 'Currency'
        
class ShipmentCharge(models.Model):
    location = models.CharField(max_length = 200)
    inner_charge = models.PositiveIntegerField()
    outer_charge = models.PositiveIntegerField()

    def __str__(self):
        return self.location
    # def Charge(self):
    #     return f'Inner {self.location} - {self.inner_charge} Outer {self.location} - {self.outer_charge}'
    