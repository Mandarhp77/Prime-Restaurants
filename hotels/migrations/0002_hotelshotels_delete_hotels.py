# Generated by Django 4.2 on 2023-06-22 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("hotels", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="HotelsHotels",
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
                ("name", models.CharField(max_length=50)),
                ("location", models.CharField(max_length=50)),
                ("items", models.CharField(max_length=50)),
                ("lat_long", models.CharField(max_length=50)),
                ("full_details", models.CharField(max_length=50)),
            ],
            options={"db_table": "hotels_hotels", "managed": False,},
        ),
        migrations.DeleteModel(name="Hotels",),
    ]
