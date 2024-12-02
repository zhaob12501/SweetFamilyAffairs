from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import HouseholdTaskTypeViewSet, HouseholdTaskViewSet, TaskCompletionViewSet, RedeemItemViewSet, PointsHistoryViewSet, PointsRedeemViewSet

router = DefaultRouter()
router.register(r'house_hold_tasks_type', HouseholdTaskTypeViewSet)
router.register(r'house_hold_tasks', HouseholdTaskViewSet)
router.register(r'task_completions', TaskCompletionViewSet)
router.register(r'redeem_items', RedeemItemViewSet)
router.register(r'points_history', PointsHistoryViewSet)
router.register(r'points_redeem', PointsRedeemViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
