# Generated by Django 4.2.8 on 2024-02-15 16:24

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("attendance", "0050_classattendancebybsm_date_created_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="classattendance",
            old_name="date_created",
            new_name="date_updated",
        ),
        migrations.RenameField(
            model_name="classattendancebybsm",
            old_name="date_created",
            new_name="date_updated",
        ),
        migrations.RenameField(
            model_name="classattendancewithgeolocation",
            old_name="date_created",
            new_name="date_updated",
        ),
    ]
