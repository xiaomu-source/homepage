"""
URL configuration for server project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
import re
from urllib.parse import urlsplit

from django.conf import settings
from django.core.exceptions import ImproperlyConfigured
from django.urls import path, include, re_path
from django.views.static import serve
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

# 文档页面
doc_view = get_schema_view(
    openapi.Info(
        title="接口文档",
        default_version="v1",
        description="接口文档",
        contact=openapi.Contact(email="mrhuanghs@126.com"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny,],
)

urlpatterns = [
    path("v1/blog/", include("blog.urls")),
    path("v1/sys/", include("system.urls")),
    path("v1/common/", include("common.urls")),
    path("v1/dev/", include("develop.urls")),
]

if settings.SWAGGER:
    urlpatterns.append(re_path(r"^docs/swagger/$", doc_view.with_ui("swagger", cache_timeout=0)))


def static(prefix, view=serve, **kwargs):
    """重载掉 from django.conf.urls.static ，这样生产环境也可以支持前端资源"""
    if not prefix:
        raise ImproperlyConfigured("Empty static prefix not permitted")
    if urlsplit(prefix).netloc:
        # No-op if a non-local prefix.
        return []
    return [re_path(r"^%s(?P<path>.*)$" % re.escape(prefix.lstrip("/")), view, kwargs=kwargs)]


urlpatterns += static("media", document_root=settings.MEDIA_ROOT)
urlpatterns += static("static", document_root=settings.STATIC_ROOT)
urlpatterns += static("docs", document_root=settings.DOCS_ROOT)