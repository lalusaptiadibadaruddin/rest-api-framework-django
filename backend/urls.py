from django.urls import path, include
from .views import ArticleViewSet
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register('articles', ArticleViewSet, basename="articles")
urlpatterns = [
    path('api/', include(router.urls))
]
