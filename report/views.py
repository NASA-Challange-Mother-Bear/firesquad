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
from utils.label_image import classify_image


class ReportViewSet(viewsets.ModelViewSet):
    queryset = Report.objects.all()
    serializer_class = ReportSerializer
    filter_class = ReportFilter


def fromDataUrlToFile(data: str):
    if data is None:
        return None

    format, imgstr = data.split(';base64,')
    ext = format.split('/')[-1]

    return ContentFile(base64.b64decode(imgstr), name='temp.' + ext)


@api_view(["POST"])
def report_post(request):
    post = request.data
    photo = fromDataUrlToFile(post.get("photo", None))
    geolocation = Point(*post["geolocation"])
    type = post["type"]
    rep = Report(photo=photo, geolocation=geolocation, type=type, user=request.user)
    rep.save()

    if photo:
        ret = classify_image(rep.photo.file.name)
        print(ret)

        rep.status = 1 if ret == "else" or ret == "forest" else 2

        rep.save()

    return Response(ReportSerializer(rep).data)
