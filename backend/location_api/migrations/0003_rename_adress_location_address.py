# Generated by Django 4.2.2 on 2023-06-12 00:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("location_api", "0002_rename_langitude_location_latitude"),
    ]

    operations = [
        migrations.RenameField(
            model_name="location",
            old_name="adress",
            new_name="address",
        ),
    ]
