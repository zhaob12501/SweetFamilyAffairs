from django.urls import path, include
from rest_framework.routers import DefaultRouter

urlpatterns = [
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('apis/', include('apis.urls')),
]
