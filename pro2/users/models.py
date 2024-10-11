from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=20, unique=True)
    password = models.CharField(max_length=128)
    phone = models.CharField(max_length=15,blank=True)
    address = models.CharField(max_length=300,blank=True)
    hobbies = models.CharField(max_length=300,blank=True)
    interests = models.CharField(max_length=255, null=True, blank=True)
    def __str__(self):
        return self.username

