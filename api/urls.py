from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import HouseholdTaskViewSet, TaskCompletionViewSet, RedeemItemViewSet, PointsHistoryViewSet, PointsRedeemViewSet, weixin_login

router = DefaultRouter()
router.register(r'householdtasks', HouseholdTaskViewSet)
router.register(r'taskcompletions', TaskCompletionViewSet)
router.register(r'redeemitems', RedeemItemViewSet)
router.register(r'pointshistory', PointsHistoryViewSet)
router.register(r'pointsredeem', PointsRedeemViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('login/weixin/', weixin_login, name='weixin_login'),
]
