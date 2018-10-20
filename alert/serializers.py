from rest_framework_gis.serializers import GeoFeatureModelSerializer

from alert.models import Alert


class AlertSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = Alert
        fields = ('timestamp', 'active', 'id')
        geo_field = 'geolocation'
