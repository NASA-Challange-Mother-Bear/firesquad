from django.contrib.auth.models import User
# Create your views here.
from rest_framework import viewsets

from user.filters import UserFilter
from user.serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_class = UserFilter


