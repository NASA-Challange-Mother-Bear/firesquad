# Create your views here.

import base64

from django.contrib.gis.geos import Point
from django.core.files.base import ContentFile
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response

from report.filters import ReportFilter
from report.models import Report
from report.serializers import ReportSerializer


class ReportViewSet(viewsets.ModelViewSet):
    queryset = Report.objects.all()
    serializer_class = ReportSerializer
    filter_class = ReportFilter


def fromDataUrlToFile(data):
    format, imgstr = data.split(';base64,')
    ext = format.split('/')[-1]

    return ContentFile(base64.b64decode(imgstr), name='temp.' + ext)


@api_view(["POST"])
def report_post(request):
    post = request.data
    photos = [fromDataUrlToFile(v) for v in post.get("images", [])]
    geolocation = Point(*post["geolocation"])
    type = post["type"]
    rep = Report(photos=photos, geolocation=geolocation, type=type, user=request.user)
    rep.save()
    return Response(ReportSerializer(rep).data)
