from django.urls import path, include
from rest_framework_nested import routers

from utils.utils import register
from .views import CodeViewSet, ModelViewSet

v1_code_router = routers.SimpleRouter()
v1_model_router = routers.SimpleRouter()

register(
    v1_code_router,
    [
        ("codes", CodeViewSet),
    ]
)

register(
    v1_model_router,
    [
        ("model", ModelViewSet),
    ]
)

urlpatterns = [
    path("", include(v1_code_router.urls)),
    path("", include(v1_model_router.urls)),
]