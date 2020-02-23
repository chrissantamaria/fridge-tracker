from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User


class Item(models.Model):
    name = models.CharField(max_length=200)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    time_entered = models.DateTimeField(default=now)
    expiration_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.name
