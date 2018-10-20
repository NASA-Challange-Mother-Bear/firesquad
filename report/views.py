from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets

from report.filters import ReportFilter
from report.models import Report
from report.serializers import ReportSerializer


class ReportViewSet(viewsets.ModelViewSet):
    queryset = Report.objects.all()
    serializer_class = ReportSerializer
    filter_class = ReportFilter
