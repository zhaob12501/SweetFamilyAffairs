from django.urls import path, include, re_path

urlpatterns = [
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('', include('items.urls')),
]
