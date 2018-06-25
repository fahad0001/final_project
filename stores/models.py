from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Store(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    lat = models.DecimalField(max_digits=50, decimal_places=20)
    long = models.DecimalField(max_digits=50, decimal_places=20)
    type = models.CharField(max_length=30)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name
