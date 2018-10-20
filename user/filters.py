import rest_framework_filters as filters
from django.contrib.auth.models import User


class UserFilter(filters.FilterSet):
    class Meta:
        model = User
        fields = {
            "username": "__all__",
            "email": "__all__",
        }
