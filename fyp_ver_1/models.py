from django.db import models
from django.contrib.auth.models import AbstractUser
from django import forms
# Create your models here.


class Contact(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=50)
    subject = models.CharField(max_length=30)
    message = models.CharField(max_length=128)

    def __str__(self):
        return self.name


class User(AbstractUser):
    is_Buyer = models.BooleanField(default=False)
    is_Seller = models.BooleanField(default=False)



