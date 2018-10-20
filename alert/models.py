from django.contrib.gis.db import models
from django.utils import timezone


# Create your models here.

class Alert(models.Model):
    timestamp = models.DateTimeField(default=timezone.now)
    geolocation = models.PointField(dim=2)

