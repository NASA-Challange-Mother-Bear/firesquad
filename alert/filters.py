import rest_framework_filters as filters
from rest_framework_gis.filters import GeoFilterSet

from alert.models import Alert


class AlertFilter(filters.FilterSet, GeoFilterSet):
    class Meta:
        model = Alert
        fields = {
            "timestamp": "__all__",
            "geolocation": "__all__"
        }