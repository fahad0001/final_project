from django.db import models
from stores.models import Store


class Category(models.Model):
    id = models.AutoField()
    name = models.CharField()


class Product(models.Model):
    id = models.AutoField()
    name = models.CharField()
    price = models.DecimalField()
    image = models.ImageField()
    category = models.ForeignKey(Category, default='Default', on_delete=None, blank=False)
    store = models.ForeignKey(Store, on_delete=models.CASCADE, blank=False, null=False)
