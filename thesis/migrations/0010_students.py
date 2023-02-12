# Generated by Django 4.1.1 on 2022-12-06 15:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("thesis", "0009_alter_data_cap1_alter_data_cap2_alter_data_cap3_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="students",
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
                ("studentID", models.CharField(max_length=100, null=True)),
                ("firstname", models.CharField(max_length=100, null=True)),
                ("lastname", models.CharField(max_length=100, null=True)),
                ("phone", models.PositiveBigIntegerField(null=True)),
                ("email", models.CharField(max_length=100, null=True)),
                ("date_created", models.DateTimeField(auto_now_add=True, null=True)),
                (
                    "user",
                    models.OneToOneField(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
