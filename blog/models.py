from django.db import models
from django_summernote.fields import SummernoteTextField
import uuid
from PIL import Image
# Create your models here.

class Blog(models.Model):
    id = models.UUIDField(primary_key = True,default = uuid.uuid4,editable = False)
    title = models.CharField(max_length = 300)
    image = models.ImageField(upload_to = 'blog_image')
    detail = SummernoteTextField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(blank = True,null = True)

    def __str__(self):
        return self.title
    def save(self,*args,**kwargs):
        super(Blog,self).save(*args,**kwargs)
        path = self.image.path
        image = Image.open(path)
        if image.height > 200 or image.width > 330:
            output_size = (330,200)
            image.thumbnail(output_size)
            image.save(path)
    class Meta:
        ordering = ['-created_at',]
    def Detail(self):
        detail = self.detail.split(' ')
        return ' '.join(detail[:15])
