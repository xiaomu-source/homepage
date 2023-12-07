from django.urls import path, include, re_path
from rest_framework_nested import routers

from common.views import FileViewSet, download_file, delete_file
from utils.utils import register

v1_common_router = routers.SimpleRouter()
register(
    v1_common_router,
    [
        ("files", FileViewSet),
    ]
)

urlpatterns = [
    path("", include(v1_common_router.urls)),
    re_path(r'^download/(?P<filename>.*?)/$', download_file, name='download_file'),
    re_path(r'^delete/(?P<filename>.*?)/$', delete_file, name='delete_file'),
]
