from alert.views import AlertViewSet
from report.views import ReportViewSet
from user.views import UserViewSet

routes = [
    ('user', UserViewSet, 'user'),

]

url_patterns = [

]