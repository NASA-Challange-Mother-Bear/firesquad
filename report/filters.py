import rest_framework_filters as filters
from django.contrib.auth.models import User
from django.contrib.gis.db import models
from django.contrib.postgres.fields import ArrayField
from rest_framework_gis.filters import GeoFilterSet, GeometryFilter

from alert.models import Alert
from report.models import Report
from user.filters import UserFilter
from utils.filters import ArrayFilter


class ReportFilter(filters.FilterSet):
    user = filters.RelatedFilter(UserFilter, queryset=User.objects.all())

    class Meta:
        model = Report
        fields = {
            "photos": "__all__",
            "geolocation": "__all__",
            "timestamp": "__all__",
            "status": "__all__",
            "type": "__all__",
            "user": "__all__",
            "alert": "__all__",
            'id': '__all__'
        }

        filter_overrides = {
            models.PointField: {
                "filter_class": GeometryFilter
            },
            ArrayField: {
                "filter_class": ArrayFilter(filters.CharFilter)
            }
        }
