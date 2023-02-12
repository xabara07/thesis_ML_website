# Generated by Django 4.1.1 on 2022-10-25 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("thesis", "0007_alter_data_year"),
    ]

    operations = [
        migrations.AlterField(
            model_name="data",
            name="year",
            field=models.PositiveBigIntegerField(
                choices=[(2, "2nd Year"), (3, "3rd Year"), (4, "4th Year")], null=True
            ),
        ),
    ]