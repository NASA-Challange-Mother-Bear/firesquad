import json

from django.contrib.auth.models import User
# Create your views here.
from rest_framework import viewsets
from rest_framework.decorators import action, api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from django.http.response import HttpResponseBadRequest
from rest_framework_jwt.serializers import JSONWebTokenSerializer, jwt_payload_handler, jwt_encode_handler

from user.filters import UserFilter
from user.serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_class = UserFilter


#
# class UserRegisterViewSet(viewsets.ViewSet):
#     permission_classes = (AllowAny,)
#     http_method_names = ('POST',)
#
#
#
#
#     def retrieve(self, request):
#         return Response(None)

@api_view(['POST', ])
@permission_classes((AllowAny,))
def register(request):
    post = request.data
    username = post.get("username", None)
    password = post.get("password", None)
    email = post.get("email", None)
    if username is None or password is None or email is None:
        return HttpResponseBadRequest()
    user = User.objects.create_user(username, password)
    user.email = email
    user.save()
    return Response({
        "user": UserSerializer(user, context={
            "request": request
        }).data,
        "token": jwt_encode_handler(jwt_payload_handler(user))
    })
