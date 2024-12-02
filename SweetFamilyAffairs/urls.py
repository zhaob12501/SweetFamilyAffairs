from django.urls import path, include, re_path
from django.urls import path, include
from rest_framework.routers import DefaultRouter

urlpatterns = [
    path('', include('users.urls')),
    path('api/', include('items.urls')),
]
