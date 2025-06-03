from django.db import models
from django_summernote.fields import SummernoteTextField
from PIL import Image

class Position(models.Model):
    name = models.CharField(max_length = 100)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = 'Position'    

class AboutUs(models.Model):
    name = models.CharField(max_length = 200)
    logo = models.ImageField(upload_to = 'logo',blank = True,null = True)
    established_at = models.DateField()
    location = models.CharField(max_length = 300,blank = True,null = True)
    phone = models.CharField(max_length = 12,blank = True,null = True)
    email = models.EmailField(blank = True,null = True,unique = True)
    detail = SummernoteTextField()
    policies = SummernoteTextField(blank = True)

    class Meta:
        verbose_name_plural = 'About Us'

    def __str__(self):
        return self.name
    def Detail(self):
        detail = self.detail.split(' ')
        if len(detail) > 20:
            detail = self.detail[:20]
        return ' '.join(detail)
    def save(self,*args,**kwargs):
        super(AboutUs,self).save(*args,**kwargs)
        if self.logo:
            logo = Image.open(self.logo.path)
            if logo.height > 44 or logo.width > 150:
                output_size = (150,44)
                logo.thumbnail(output_size)
                logo.save(self.logo.path)

class Employee(models.Model):
    name = models.CharField(max_length = 300)
    image = models.ImageField(upload_to = 'employee_images',blank = True,null = True)
    position = models.ForeignKey(Position,on_delete = models.SET_NULL,blank = True,null = True)
    EMPLOYEE_TYPE = [
        ('Full Time','Full Time'),
        ('Part Time','Part Time'),
    ]
    employee_type = models.CharField(choices = EMPLOYEE_TYPE,max_length = 11,default = 'Full Time')
    cell = models.CharField(max_length = 11)
    email = models.EmailField()

    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = 'Employee'
    def save(self,*args,**kwargs):
        super(Employee,self).save(*args,**kwargs)
        if self.image:
            image = Image.open(self.image.path)
            if image.height > 400 or image.width > 330:
                output_size = (330,440)
                image.thumbnail(output_size)
                image.save(self.image.path)

class OurPartner(models.Model):
    name = models.CharField(max_length = 200)
    logo = models.ImageField(upload_to = 'partner_logo',blank = True,null = True,)
    url = models.URLField(blank = True,null =True)

    def __str__(self):
        return self.name
    def save(self,*args,**kwargs):
        super(OurPartner,self).save(*args,**kwargs)
        if self.logo:
            logo = Image.open(self.logo.path)
            if logo.height > 150 or logo.width > 150:
                output_size = (150,150)
                logo.thumbnail(output_size)
                logo.save(self.logo.path)
                    



