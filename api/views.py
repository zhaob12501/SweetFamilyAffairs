from rest_framework import viewsets
from .models import HouseholdTask, TaskCompletion, RedeemItem, PointsHistory, PointsRedeem
from .serializers import HouseholdTaskSerializer, TaskCompletionSerializer, RedeemItemSerializer, PointsHistorySerializer, PointsRedeemSerializer


class HouseholdTaskViewSet(viewsets.ModelViewSet):
    """
    家务任务视图集
    """
    queryset = HouseholdTask.objects.all()
    serializer_class = HouseholdTaskSerializer


class TaskCompletionViewSet(viewsets.ModelViewSet):
    """
    任务完成记录视图集
    """
    queryset = TaskCompletion.objects.all()
    serializer_class = TaskCompletionSerializer


class RedeemItemViewSet(viewsets.ModelViewSet):
    """
    兑换物品视图集
    """
    queryset = RedeemItem.objects.all()
    serializer_class = RedeemItemSerializer


class PointsHistoryViewSet(viewsets.ModelViewSet):
    """
    积分历史视图集
    """
    queryset = PointsHistory.objects.all()
    serializer_class = PointsHistorySerializer


class PointsRedeemViewSet(viewsets.ModelViewSet):
    """
    积分兑换视图集
    """
    queryset = PointsRedeem.objects.all()
    serializer_class = PointsRedeemSerializer


from django.conf import settings
from django.http import HttpResponseRedirect
from social_core.actions import do_auth
from social_django.utils import load_backend, load_strategy


def weixin_login(request):
    """
    微信登录回调处理
    """
    backend = load_backend(load_strategy(request),
                           settings.AUTHENTICATION_BACKENDS,
                           'weixin',
                           request=request)
    return do_auth(backend, request)
