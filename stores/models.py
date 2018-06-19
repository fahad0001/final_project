from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Store(models.Model):
    user = models.ForeignKey(User)
    id = models.AutoField()
    name = models.CharField(max_length=30)
    lat = models.DecimalField()
    long = models.DecimalField()
    type = models.CharField(max_length=30)