from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login, name='login'),  # Сторінка входу
    path('signup/', views.signup, name='signup'),  # Сторінка реєстрації
    path('logout/', views.logout, name='logout'),  # Сторінка виходу
    path('test_token/', views.test_token, name='test_token'),  # Тест токенів
]
