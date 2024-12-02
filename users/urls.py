from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import FimalyViewSet, UserViewSet, WxAuthView

router = DefaultRouter()
router.register(r'family', FimalyViewSet)
router.register(r'user', UserViewSet)
urlpatterns = [
    path('', include(router.urls)),
    path('auth/', WxAuthView.as_view())
]