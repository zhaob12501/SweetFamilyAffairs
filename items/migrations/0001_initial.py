# Generated by Django 5.1.3 on 2024-12-01 21:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="HouseholdTask",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "task_name",
                    models.CharField(max_length=100, verbose_name="任务名称"),
                ),
                ("points_value", models.IntegerField(verbose_name="积分值")),
                (
                    "description",
                    models.TextField(blank=True, null=True, verbose_name="描述"),
                ),
            ],
        ),
        migrations.CreateModel(
            name="PointsHistory",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("points_change", models.IntegerField(verbose_name="积分变化")),
                (
                    "change_reason",
                    models.CharField(max_length=100, verbose_name="变化原因"),
                ),
                (
                    "change_time",
                    models.DateTimeField(auto_now_add=True, verbose_name="变化时间"),
                ),
            ],
        ),
        migrations.CreateModel(
            name="PointsRedeem",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("points_used", models.IntegerField(verbose_name="使用的积分")),
                (
                    "redeem_time",
                    models.DateTimeField(auto_now_add=True, verbose_name="兑换时间"),
                ),
            ],
        ),
        migrations.CreateModel(
            name="RedeemItem",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "item_name",
                    models.CharField(max_length=100, verbose_name="物品名称"),
                ),
                ("points_required", models.IntegerField(verbose_name="所需积分")),
                (
                    "description",
                    models.TextField(blank=True, null=True, verbose_name="描述"),
                ),
                ("stock_quantity", models.IntegerField(verbose_name="库存数量")),
                (
                    "status",
                    models.CharField(
                        choices=[("available", "可兑换"), ("sold_out", "已兑换完")],
                        default="available",
                        max_length=20,
                        verbose_name="兑换状态",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="TaskCompletion",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "completion_time",
                    models.DateTimeField(auto_now_add=True, verbose_name="完成时间"),
                ),
                ("points_earned", models.IntegerField(verbose_name="获得积分")),
            ],
        ),
    ]
