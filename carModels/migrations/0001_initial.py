# Generated by Django 4.2.3 on 2023-10-14 19:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("companies", "0001_initial"),
        ("carTrims", "0001_initial"),
        ("carTypes", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="CarModels",
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
                ("model_name", models.CharField(max_length=200)),
                ("date", models.DateTimeField(auto_now_add=True)),
                ("price", models.DecimalField(decimal_places=4, max_digits=15)),
                ("description", models.TextField(blank=True)),
                (
                    "model_image",
                    models.ImageField(
                        blank=True,
                        default="modelImages/model.jpeg",
                        upload_to="modelImages",
                    ),
                ),
                (
                    "company",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="companies.companies",
                    ),
                ),
                (
                    "trims",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="carTrims.cartrims",
                    ),
                ),
                (
                    "type",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="carTypes.cartypes",
                    ),
                ),
            ],
        ),
    ]
