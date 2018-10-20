import os
import uuid

from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.gis.db import models
from django.contrib.postgres.fields import ArrayField
from django.utils import timezone
from django.utils.translation import gettext as _


# Create your models here.


def report_location(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)
    return os.path.join(settings.MEDIA_ROOT, "report", filename)


class Report(models.Model):
    STATUS_CHOICES = (
        (0, _("Processing")),
        (1, _("Rejected")),
        (2, _("Accepted"))
    )

    TYPE_CHOICES = (
        (0, _("Forest Fire")),
        (1, _("Fire Hazard"))
    )

    photos = ArrayField(models.ImageField(upload_to=report_location), blank=True)
    geolocation = models.PointField(dim=2)
    timestamp = models.DateTimeField(default=timezone.now)
    status = models.IntegerField(choices=STATUS_CHOICES, default=0)
    type = models.IntegerField(choices=TYPE_CHOICES)
    user = models.ForeignKey(User, null=False, blank=False, on_delete=models.CASCADE)
    alert = models.ForeignKey("alert.Alert", null=True, blank=True, on_delete=models.CASCADE, related_name="alerts")
