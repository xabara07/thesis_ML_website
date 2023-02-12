# Generated by Django 4.1.5 on 2023-01-08 09:47

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("thesis", "0030_remove_student_stud_age_remove_student_stud_sex"),
    ]

    operations = [
        migrations.AddField(
            model_name="student",
            name="stud_age",
            field=models.PositiveBigIntegerField(
                null=True,
                validators=[
                    django.core.validators.MinValueValidator(17),
                    django.core.validators.MaxValueValidator(40),
                ],
            ),
        ),
        migrations.AddField(
            model_name="student",
            name="stud_sex",
            field=models.PositiveBigIntegerField(
                choices=[(0, "Female"), (1, "Male")], null=True
            ),
        ),
        migrations.AlterField(
            model_name="student",
            name="email",
            field=models.CharField(max_length=100, null=True, verbose_name="Sex"),
        ),
        migrations.AlterField(
            model_name="student",
            name="phone",
            field=models.PositiveBigIntegerField(null=True, verbose_name="Age"),
        ),
    ]
