from django.urls import path, include
from rest_framework_nested import routers

from blog.views import (AdminPostViewSet, ClientPostViewSet, AdminMessageViewSet, ClientMessageViewSet, AdminPortfolioViewSet, ClientPortfolioViewSet, )
from utils.utils import register

v1_blog_router = routers.SimpleRouter()
register(
    v1_blog_router,
    [
        ("blog_articles", AdminPostViewSet),
        ("blog_articles/client", ClientPostViewSet),
        ("messages", AdminMessageViewSet),
        ("messages/client", ClientMessageViewSet),
        ("portfolios", AdminPortfolioViewSet),
        ("portfolios/client", ClientPortfolioViewSet),
    ]
)

urlpatterns = [
    path("", include(v1_blog_router.urls)),
]


