# Generated by Django 4.2.11 on 2024-03-25 22:39

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("myApp", "0002_delete_venue_alter_artist_description"),
    ]

    operations = [
        migrations.AddField(
            model_name="artist",
            name="venue",
            field=models.CharField(default="SOME STRING", max_length=100),
        ),
    ]
