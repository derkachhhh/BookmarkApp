from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import BookmarkViewSet

# Ініціалізація DefaultRouter
router = DefaultRouter()
router.register(r'', BookmarkViewSet, basename='bookmarks')  # Без префіксу

# Основні маршрути
urlpatterns = [
    path('', include(router.urls)),  # Інтеграція маршрутів DefaultRouter
]
