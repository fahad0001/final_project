from django.db import models

from django.contrib.auth.models import User


class Invitation(models.Model):
    from_user = models.ForeignKey(User, on_delete=False, related_name="invitation_sent")
    to_user = models.ForeignKey(User, on_delete=False, related_name="invitation_received")
    message = models.CharField(max_length=300)
    timestamp = models.DateTimeField(auto_now_add=True)