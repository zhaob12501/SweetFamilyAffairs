from django.http import JsonResponse
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .models import HouseholdTask, HouseholdTaskType, TaskCompletion, RedeemItem, PointsHistory, PointsRedeem
from .serializers import HouseholdTaskTypeSerializer, HouseholdTaskSerializer, TaskCompletionSerializer, RedeemItemSerializer, PointsHistorySerializer, PointsRedeemSerializer


class FamilyViewSetMixin:
    """ 使所有模型必须只能查询到属于它家庭的数据 """
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = super().get_queryset()
        if queryset.exists() and self.request.user.family.id != 1:
            return queryset.filter(family=self.request.user.family)
        return queryset.none()


class HouseholdTaskTypeViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = HouseholdTaskTypeSerializer
    queryset = HouseholdTaskType.objects.all()


class HouseholdTaskViewSet(FamilyViewSetMixin, viewsets.ModelViewSet):
    """
    家务任务视图集
    """
    queryset = HouseholdTask.objects.all()
    serializer_class = HouseholdTaskSerializer


class TaskCompletionViewSet(FamilyViewSetMixin, viewsets.ModelViewSet):
    """
    任务完成记录视图集
    """
    queryset = TaskCompletion.objects.all()
    serializer_class = TaskCompletionSerializer


class RedeemItemViewSet(FamilyViewSetMixin, viewsets.ModelViewSet):
    """
    兑换物品视图集
    """
    queryset = RedeemItem.objects.all()
    serializer_class = RedeemItemSerializer


class PointsHistoryViewSet(FamilyViewSetMixin, viewsets.ModelViewSet):
    """
    积分历史视图集
    """
    queryset = PointsHistory.objects.all()
    serializer_class = PointsHistorySerializer


class PointsRedeemViewSet(FamilyViewSetMixin, viewsets.ModelViewSet):
    """
    积分兑换视图集
    """
    queryset = PointsRedeem.objects.all()
    serializer_class = PointsRedeemSerializer
