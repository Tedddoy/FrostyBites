from django.db import models
from django.contrib.auth.models import User

class Services(models.Model):
    service_name = models.CharField(max_length=255, null=True)
    details = models.CharField(max_length=255, null=True)
    price = models.IntegerField(null=True)

    def __str__(self):
        return f"{self.service_name}"
    

class Appointment(models.Model):
    service = models.ForeignKey(Services, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)  # Make it nullable
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Appointment for {self.service.service_name} on {self.date} at {self.time}"