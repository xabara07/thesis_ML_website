# Generated by Django 4.1.1 on 2022-10-22 23:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("thesis", "0004_alter_data_year"),
    ]

    operations = [
        migrations.AlterField(
            model_name="data",
            name="predictions",
            field=models.PositiveBigIntegerField(blank=True),
        ),
    ]