from django.db import models

# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length = 200)
    email = models.EmailField(blank = True,null = True)
    phone = models.CharField(max_length = 11,blank = True,null = True)
    subject = models.CharField(max_length = 300)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.name

class Feedback(models.Model):
    name = models.CharField(max_length = 100)
    occupation = models.CharField(max_length = 50,blank = True,null = True)
    feedback = models.TextField()

    def __str__(self):
        return self.name
    
class Subscribe(models.Model):
    email = models.EmailField(unique = True)
    created_at = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.email
    
    