from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets

from alert.filters import AlertFilter
from alert.models import Alert
from alert.serializers import AlertSerializer


class AlertViewSet(viewsets.ModelViewSet):
    queryset = Alert.objects.all()
    serializer_class = AlertSerializer
    filter_class = AlertFilter
