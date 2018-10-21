"""nasa_challange URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from rest_framework_jwt.views import obtain_jwt_token

import alert.urls as alertUrls
import report.urls as reportUrls
import user.urls as userUrls

router = routers.DefaultRouter()

routeLists = [
    alertUrls.routes,
    reportUrls.routes,
    userUrls.routes,
]

for routeList in routeLists:
    for route in routeList:
        base_name = None if len(route) <= 2 else route[2]
        router.register(route[0], route[1], base_name=base_name)

urlpatterns = [
    path('api/', include(router.urls)),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api-token-auth/', obtain_jwt_token),
    path('', include(reportUrls)),
    path('', include(userUrls))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
