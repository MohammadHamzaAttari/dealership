# Generated by Django 4.2.3 on 2023-10-15 06:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("carModels", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="carmodels", old_name="type", new_name="car_type",
        ),
    ]