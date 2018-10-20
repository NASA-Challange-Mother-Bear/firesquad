import rest_framework_filters as filters
from django.contrib.gis.db import models
from rest_framework_gis.filters import GeoFilterSet, GeometryFilter

from alert.models import Alert


class AlertFilter(filters.FilterSet):
    class Meta:
        model = Alert
        fields = {
            "timestamp": "__all__",
            "geolocation": "__all__",
            "active": "__all__"
        }

        filter_overrides = {
            models.PointField: {
                "filter_class": GeometryFilter
            }
        }
