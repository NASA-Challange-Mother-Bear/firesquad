from django.urls import path

from report.views import ReportViewSet, report_post

routes = [
    ('report', ReportViewSet, 'report'),
]

urlpatterns = [
    path("api/report_post/", report_post, name="report_post")
]
