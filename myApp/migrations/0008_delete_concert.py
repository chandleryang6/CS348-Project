# Generated by Django 4.2.11 on 2024-03-26 01:10

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("myApp", "0007_alter_concert_venue_delete_venue"),
    ]

    operations = [
        migrations.DeleteModel(
            name="Concert",
        ),
    ]
