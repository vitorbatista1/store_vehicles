# Generated by Django 5.1.4 on 2025-01-21 17:36

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("cars", "0008_carinventory"),
    ]

    operations = [
        migrations.AlterField(
            model_name="carinventory",
            name="cars_value",
            field=models.FloatField(default=0.0),
        ),
    ]
