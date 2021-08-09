from knox import views as knox_views
from .views import LoginAPI, RegisterAPI
from django.urls import path, include

urlpatterns = [
    path('api/register/', RegisterAPI.as_view(), name='register'),
    path('api/login/', LoginAPI.as_view(), name='login'),
]