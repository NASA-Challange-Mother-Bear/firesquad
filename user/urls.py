from django.urls import path
from user.views import UserViewSet, register

routes = [
    ('user', UserViewSet, 'user')

]

urlpatterns = [
    path('api/register/', register, name='register')
]
