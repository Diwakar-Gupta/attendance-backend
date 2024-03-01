# Generated by Django 4.2.7 on 2023-12-09 14:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('attendance', '0038_alter_classattendancebybsm_marked_by_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='classattendance',
            options={'permissions': [('can_mark_attendance', 'Can Mark Attendance'), ('can_send_notifications', 'Can Send Notifications'), ('verify_false_attempt', 'Verify False Attempt GeoLocation')]},
        ),
        migrations.AddField(
            model_name='classattendancewithgeolocation',
            name='verified_by',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]