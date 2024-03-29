# Generated by Django 4.2.2 on 2023-06-11 23:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Location",
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
                ("fsq_id", models.CharField(max_length=100)),
                ("langitude", models.FloatField()),
                ("longitude", models.FloatField()),
                ("adress", models.TextField()),
                ("country", models.CharField(max_length=30)),
                ("region", models.CharField(max_length=50)),
                ("name", models.CharField(max_length=155)),
            ],
        ),
    ]
