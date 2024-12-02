from django.urls import path, include, re_path
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from users.views import WxUserLoginAPIView, WxUserViewSet

router = DefaultRouter()
router.register(r'users', WxUserViewSet)
urlpatterns = [
    path('', include('items.urls')),
    path('', include(router.urls)),
    path('login/', WxUserLoginAPIView.as_view(), name='login'),
]
