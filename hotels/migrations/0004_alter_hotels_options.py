# Generated by Django 4.2 on 2023-06-23 06:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("hotels", "0003_hotels_delete_hotelshotels"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="hotels", options={"managed": False, "verbose_name_plural": "Hotels"},
        ),
    ]
