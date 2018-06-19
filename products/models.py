from django.db import models
from stores.models import Store


class Category(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)


class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    price = models.DecimalField(max_digits=5, decimal_places=5)
    image = models.ImageField()
    category = models.ForeignKey(Category, default='Default', on_delete=None, blank=False)
    store = models.ForeignKey(Store, on_delete=models.CASCADE, blank=False, null=False)
