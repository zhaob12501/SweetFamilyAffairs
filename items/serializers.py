from rest_framework import serializers
from .models import HouseholdTask, HouseholdTaskType, TaskCompletion, RedeemItem, PointsHistory, PointsRedeem


class HouseholdTaskTypeSerializer(serializers.ModelSerializer):
    """
    家务类型序列化器，用于将 HouseholdTaskType 模型转换为 JSON 格式。
    """

    class Meta:
        model = HouseholdTaskType
        fields = '__all__'  # 或者指定具体字段，如 ['id', 'type_name', 'description']


class HouseholdTaskSerializer(serializers.ModelSerializer):
    """
    家务任务序列化器，用于将 HouseholdTask 模型转换为 JSON 格式。
    """
    task_type = HouseholdTaskTypeSerializer()  # 嵌套序列化器

    class Meta:
        model = HouseholdTask
        fields = '__all__'  # 或者指定具体字段，如 ['id', 'task_name', 'points_value', 'description', 'task_type']

    def create(self, validated_data):
        """
        重写 create 方法以处理嵌套序列化器。
        """
        task_type_data = validated_data.pop('task_type')
        task_type, created = HouseholdTaskType.objects.get_or_create(**task_type_data)
        household_task = HouseholdTask.objects.create(task_type=task_type, **validated_data)
        return household_task

    def update(self, instance, validated_data):
        """
        重写 update 方法以处理嵌套序列化器。
        """
        task_type_data = validated_data.pop('task_type', None)
        if task_type_data:
            task_type, created = HouseholdTaskType.objects.get_or_create(**task_type_data)
            instance.task_type = task_type

        instance.task_name = validated_data.get('task_name', instance.task_name)
        instance.points_value = validated_data.get('points_value', instance.points_value)
        instance.description = validated_data.get('description', instance.description)
        instance.save()
        return instance

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
