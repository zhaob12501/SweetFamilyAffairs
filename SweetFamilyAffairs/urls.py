from django.urls import path, include
from rest_framework.routers import DefaultRouter

urlpatterns = [
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('', include('social_django.urls', namespace='social')),
    path('api/', include('api.urls')),
]
