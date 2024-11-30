from rest_framework import serializers
from .models import HouseholdTask, TaskCompletion, RedeemItem, PointsHistory, PointsRedeem

class HouseholdTaskSerializer(serializers.ModelSerializer):
    """
    家务任务序列化器
    """
    class Meta:
        model = HouseholdTask
        fields = '__all__'

class TaskCompletionSerializer(serializers.ModelSerializer):
    """
    任务完成记录序列化器
    """
    class Meta:
        model = TaskCompletion
        fields = '__all__'

class RedeemItemSerializer(serializers.ModelSerializer):
    """
    兑换物品序列化器
    """
    class Meta:
        model = RedeemItem
        fields = '__all__'

class PointsHistorySerializer(serializers.ModelSerializer):
    """
    积分历史序列化器
    """
    class Meta:
        model = PointsHistory
        fields = '__all__'

class PointsRedeemSerializer(serializers.ModelSerializer):
    """
    积分兑换序列化器
    """
    class Meta:
        model = PointsRedeem
        fields = '__all__'
