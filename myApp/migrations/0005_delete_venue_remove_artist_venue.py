# Generated by Django 4.2.11 on 2024-03-25 23:17

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("myApp", "0004_venue_alter_artist_venue"),
    ]

    operations = [
        migrations.DeleteModel(
            name="Venue",
        ),
        migrations.RemoveField(
            model_name="artist",
            name="venue",
        ),
    ]