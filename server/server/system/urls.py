from django.urls import path, include
from rest_framework_nested import routers

from system.views import AuthViewSet, UserViewSet, RoleViewSet, PermissionViewSet, UserOptLogViewSet, ResourceViewSet
from utils.utils import register

v1_auth_routers = routers.SimpleRouter()

register(
    v1_auth_routers,
    [
        ("auth", AuthViewSet),
        ("users", UserViewSet),
        ("roles", RoleViewSet),
        ("permissions", PermissionViewSet),
        ("users_opt_logs", UserOptLogViewSet),
        ("resources", ResourceViewSet),
    ]
)

urlpatterns = [
    path("", include(v1_auth_routers.urls))
]
