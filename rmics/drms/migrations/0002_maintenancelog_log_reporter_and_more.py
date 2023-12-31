# Generated by Django 4.1.7 on 2023-12-06 15:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ams', '0007_plantassignment'),
        ('drms', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='maintenancelog',
            name='log_reporter',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='maintenancelog',
            name='plant_of_record',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='ams.plantassignment'),
        ),
    ]
