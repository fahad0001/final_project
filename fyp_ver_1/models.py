from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class User(AbstractUser):
    is_Buyer = models.BooleanField(default=False)
    is_Seller = models.BooleanField(default=False)

