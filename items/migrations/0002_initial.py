# Generated by Django 5.1.3 on 2024-12-03 01:46

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("items", "0001_initial"),
        ("users", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name="householdtask",
            name="fimaly",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="users.family"
            ),
        ),
        migrations.AddField(
            model_name="householdtasktype",
            name="fimaly",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="users.family"
            ),
        ),
        migrations.AddField(
            model_name="householdtask",
            name="task_type",
            field=models.ForeignKey(
                default=None,
                on_delete=django.db.models.deletion.CASCADE,
                to="items.householdtasktype",
                verbose_name="任务类型",
            ),
        ),
        migrations.AddField(
            model_name="pointshistory",
            name="fimaly",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="users.family"
            ),
        ),
        migrations.AddField(
            model_name="pointshistory",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="points_history",
                to=settings.AUTH_USER_MODEL,
                verbose_name="用户",
            ),
        ),
        migrations.AddField(
            model_name="pointsredeem",
            name="fimaly",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="users.family"
            ),
        ),
        migrations.AddField(
            model_name="pointsredeem",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="points_redeem",
                to=settings.AUTH_USER_MODEL,
                verbose_name="用户",
            ),
        ),
        migrations.AddField(
            model_name="redeemitem",
            name="fimaly",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="users.family"
            ),
        ),
        migrations.AddField(
            model_name="pointsredeem",
            name="item",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="redeemed_by",
                to="items.redeemitem",
                verbose_name="物品",
            ),
        ),
        migrations.AddField(
            model_name="taskcompletion",
            name="fimaly",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="users.family"
            ),
        ),
        migrations.AddField(
            model_name="taskcompletion",
            name="task",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="completions",
                to="items.householdtask",
                verbose_name="任务",
            ),
        ),
        migrations.AddField(
            model_name="taskcompletion",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="task_completions",
                to=settings.AUTH_USER_MODEL,
                verbose_name="用户",
            ),
        ),
    ]
