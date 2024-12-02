# Generated by Django 5.1.3 on 2024-12-01 22:08

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("items", "0002_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="HouseholdTaskType",
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
                    "type_name",
                    models.CharField(max_length=100, verbose_name="类型名称"),
                ),
                (
                    "description",
                    models.TextField(blank=True, null=True, verbose_name="描述"),
                ),
            ],
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
    ]
