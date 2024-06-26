# Generated by Django 4.2.11 on 2024-03-25 23:02

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("myApp", "0003_artist_venue"),
    ]

    operations = [
        migrations.CreateModel(
            name="Venue",
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
                ("name", models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name="artist",
            name="venue",
            field=models.CharField(max_length=100),
        ),
    ]
