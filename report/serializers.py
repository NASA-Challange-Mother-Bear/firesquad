
from rest_framework_gis.serializers import GeoFeatureModelSerializer

from report.models import Report


class ReportSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = Report
        fields = ('photos', 'timestamp', 'status', 'type', 'user', 'alert')
        geo_field = 'geolocation'
