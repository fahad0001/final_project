from django.db import models
from stores.models import Store
from django.contrib.auth import get_user_model

User = get_user_model()


class Category(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Product(models.Model):

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=128,null=True)
    price = models.IntegerField()
    image = models.ImageField(upload_to='upload_to/')
    category = models.ForeignKey(Category, default='Default', on_delete=models.CASCADE, blank=False, null=False)
    store = models.ForeignKey(Store, on_delete=models.CASCADE,related_name="products", blank=False, null=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE,  null=True)

    def __str__(self):
        return self.name
