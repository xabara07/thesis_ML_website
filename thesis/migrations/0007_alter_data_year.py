# Generated by Django 4.1.1 on 2022-10-25 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("thesis", "0006_alter_data_predictions"),
    ]

    operations = [
        migrations.AlterField(
            model_name="data",
            name="year",
            field=models.CharField(
                choices=[(2, "2nd Year"), (3, "3rd Year"), (4, "4th Year")],
                max_length=20,
                null=True,
            ),
        ),
    ]
