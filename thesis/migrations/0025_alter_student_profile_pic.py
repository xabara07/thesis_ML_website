# Generated by Django 4.1.1 on 2022-12-15 04:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("thesis", "0024_alter_data_studentid_alter_student_phone_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="student",
            name="profile_pic",
            field=models.ImageField(
                blank=True, default="unknown.jpg", null=True, upload_to=""
            ),
        ),
    ]
