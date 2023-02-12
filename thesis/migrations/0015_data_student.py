# Generated by Django 4.1.1 on 2022-12-08 04:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("thesis", "0014_rename_students_student"),
    ]

    operations = [
        migrations.AddField(
            model_name="data",
            name="student",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="thesis.student",
            ),
        ),
    ]
