from django.db import models

from users.models import User, Family

class HouseholdTaskType(models.Model):
    """
    家务类型模型，用于记录各种家务任务的类型。
    - type_name: 类型的名称。
    - description: 类型的详细描述。
    """
    type_name = models.CharField(max_length=100, verbose_name="类型名称")
    description = models.TextField(blank=True, null=True, verbose_name="描述")

    def __str__(self):
        """
        返回类型的字符串表示，通常用于调试和后台管理界面。
        """
        return self.type_name


class HouseholdTask(models.Model):
    """
    家务任务模型，用于记录各种家务任务及其对应的积分值。
    - task_name: 任务的名称。
    - points_value: 完成任务后用户可以获得的积分值。
    - description: 任务的详细描述。
    - task_type: 任务所属的类型。
    - family: 与家庭(Fimaly)进行外键绑定
    """
    family = models.ForeignKey(Family, on_delete=models.CASCADE)
    task_name = models.CharField(max_length=100, verbose_name="任务名称")
    points_value = models.IntegerField(verbose_name="积分值")
    description = models.TextField(blank=True, null=True, verbose_name="描述")
    task_type = models.ForeignKey(HouseholdTaskType, on_delete=models.CASCADE, verbose_name="任务类型", default=None)

    def __str__(self):
        """
        返回任务的字符串表示，通常用于调试和后台管理界面。
        """
        return self.task_name


class TaskCompletion(models.Model):
    """
    任务完成记录模型，用于记录用户完成任务的情况。
    - user: 完成任务的用户，与用户(User)模型建立外键关联。
    - task: 完成的任务，与家务任务模型(HouseholdTask)建立外键关联。
    - completion_time: 完成任务的时间。
    - points_earned: 用户完成任务后获得的积分。
    - family: 与家庭(Fimaly)进行外键绑定
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='task_completions', verbose_name="用户")
    family = models.ForeignKey(Family, on_delete=models.CASCADE)
    task = models.ForeignKey(HouseholdTask, on_delete=models.CASCADE, related_name='completions', verbose_name="任务")
    completion_time = models.DateTimeField(auto_now_add=True, verbose_name="完成时间")
    points_earned = models.IntegerField(verbose_name="获得积分")

    def __str__(self):
        """
        返回任务完成记录的字符串表示，通常用于调试和后台管理界面。
        """
        return f"{self.user} - {self.task}"


class RedeemItem(models.Model):
    """
    兑换物品模型，用于记录可以兑换的物品及其信息。
    - item_name: 物品的名称。
    - points_required: 兑换该物品所需的积分。
    - description: 物品的详细描述。
    - stock_quantity: 物品的库存数量。
    - status: 物品的兑换状态，例如“可兑换”或“已兑换完”。
    - family: 与家庭(Fimaly)进行外键绑定
    """
    family = models.ForeignKey(Family, on_delete=models.CASCADE)
    item_name = models.CharField(max_length=100, verbose_name="物品名称")
    points_required = models.IntegerField(verbose_name="所需积分")
    description = models.TextField(blank=True, null=True, verbose_name="描述")
    stock_quantity = models.IntegerField(verbose_name="库存数量")
    status = models.CharField(max_length=20, choices=[('available', '可兑换'), ('sold_out', '已兑换完')], default='available', verbose_name="兑换状态")

    def __str__(self):
        """
        返回兑换物品的字符串表示，通常用于调试和后台管理界面。
        """
        return self.item_name


class PointsHistory(models.Model):
    """
    积分历史记录模型，用于记录用户积分的变化历史。
    - user: 发生积分变化的用户，与User模型建立外键关联。
    - points_change: 积分的变化量。
    - change_reason: 积分变化的原因。
    - change_time: 积分变化的时间。
    - family: 与家庭(Fimaly)进行外键绑定
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='points_history', verbose_name="用户")
    family = models.ForeignKey(Family, on_delete=models.CASCADE)
    points_change = models.IntegerField(verbose_name="积分变化")
    change_reason = models.CharField(max_length=100, verbose_name="变化原因")
    change_time = models.DateTimeField(auto_now_add=True, verbose_name="变化时间")

    def __str__(self):
        """
        返回积分历史记录的字符串表示，通常用于调试和后台管理界面。
        """
        return f"{self.user} - {self.points_change}"


class PointsRedeem(models.Model):
    """
    积分兑换记录模型，用于记录用户使用积分兑换物品的情况。
    - user: 兑换物品的用户，与User模型建立外键关联。
    - item: 被兑换的物品，与RedeemItem模型建立外键关联。
    - points_used: 兑换物品时使用的积分。
    - redeem_time: 兑换物品的时间。
    - family: 与家庭(Fimaly)进行外键绑定
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='points_redeem', verbose_name="用户")
    family = models.ForeignKey(Family, on_delete=models.CASCADE)
    item = models.ForeignKey(RedeemItem, on_delete=models.CASCADE, related_name='redeemed_by', verbose_name="物品")
    points_used = models.IntegerField(verbose_name="使用的积分")
    redeem_time = models.DateTimeField(auto_now_add=True, verbose_name="兑换时间")

    def __str__(self):
        """
        返回积分兑换记录的字符串表示，通常用于调试和后台管理界面。
        """
        return f"{self.user} - {self.item}"
