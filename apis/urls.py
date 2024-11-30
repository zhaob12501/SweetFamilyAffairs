from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views
from .views import ApiView

router = DefaultRouter()
router.register(r'householdtasks', views.HouseholdTaskViewSet)
router.register(r'taskcompletions', views.TaskCompletionViewSet)
router.register(r'redeemitems', views.RedeemItemViewSet)
router.register(r'pointshistory', views.PointsHistoryViewSet)
router.register(r'pointsredeem', views.PointsRedeemViewSet)

urlpatterns = [
    path('', ApiView.as_view()),
    path('', include(router.urls)),
]
