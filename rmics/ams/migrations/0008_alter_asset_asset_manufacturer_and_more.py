# Generated by Django 4.1.7 on 2023-03-28 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ams', '0007_alter_asset_asset_manufacturer_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='asset',
            name='asset_manufacturer',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='asset',
            name='asset_model',
            field=models.CharField(max_length=100),
        ),
    ]
