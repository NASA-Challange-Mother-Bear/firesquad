import rest_framework_filters as filters
from django.contrib.auth.models import User
from rest_framework_gis.filters import GeoFilterSet

from alert.models import Alert
from user.filters import UserFilter


class ReportFilter(filters.FilterSet, GeoFilterSet):
    user = filters.RelatedFilter(UserFilter, queryset=User.objects.all())

    class Meta:
        model = Alert
        fields = {
            "photos": "__all__",
            "geolocation": "__all__",
            "timestamp": "__all__",
            "status": "__all__",
            "type": "__all__",
            "user": "__all__",
            "alert": "__all__"
        }