from django.db import models
from django.contrib.auth.models import User

class Services(models.Model):
    service_name = models.CharField(max_length=255, null=True)
    details = models.CharField(max_length=255, null=True)
    price = models.IntegerField(null=True)

    def __str__(self):
        return f"{self.service_name}"

