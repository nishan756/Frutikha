from django.db import models
import uuid
from django_summernote.fields import SummernoteTextField
from PIL import Image
from django.utils.timezone import now
# Create your models here.

class Product(models.Model):
    id = models.UUIDField(primary_key = True, default = uuid.uuid4,editable = False)
    name = models.CharField(max_length = 300)
    image = models.ImageField(upload_to = 'product_image',blank = True,null = True)
    price = models.PositiveIntegerField(help_text = 'in Tk')
    UNIT = [
        ('kg','kg'),
        ('gm','gm'),
        ('pcs','pcs'),
        ('dozen','dozen'),

    ]
    unit = models.CharField(choices = UNIT,max_length = 7,default = 'kg')
    stock = models.PositiveIntegerField(default = 0)
    detail = SummernoteTextField(blank = True,null = True)
    created_at = models.DateField(auto_now_add = True)

    def __str__(self):
        return self.name
    class Meta:
        ordering = ['-created_at',]
    def save(self, *args, **kwargs):
        super(Product, self).save(*args, **kwargs)
        try:
            image = Image.open(self.image.path)
            max_width, max_height = 612, 470
            
            if image.height > max_height or image.width > max_width:
                output_size = (max_width, max_height)
                image.thumbnail(output_size) 
                image.save(self.image.path) 
        except Exception as e:
            print(f"Error processing image: {e}")



