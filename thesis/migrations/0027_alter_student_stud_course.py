# Generated by Django 4.1.5 on 2023-01-08 08:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("thesis", "0026_alter_student_stud_course_alter_student_stud_year"),
    ]

    operations = [
        migrations.AlterField(
            model_name="student",
            name="stud_course",
            field=models.PositiveBigIntegerField(
                choices=[
                    (1, "BS Community Development"),
                    (2, "BS Information Technology"),
                    (3, "BS Computer Science"),
                    (4, "BS Social Work"),
                ],
                max_length=100,
                null=True,
                verbose_name="Course",
            ),
        ),
    ]
