from django.contrib import admin
from django.urls import path, include
from bookmarkapi.views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),  # Головна сторінка
    path('bookmarks/', include('bookmarkapi.urls')),  # Маршрути bookmarkapi
    path('auth/', include('loginapp.urls')),  # Маршрути loginapp
]

