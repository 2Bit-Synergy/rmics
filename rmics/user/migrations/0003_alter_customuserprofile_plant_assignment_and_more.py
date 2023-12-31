# Generated by Django 4.1.7 on 2023-11-11 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_customuserprofile_delete_userprofile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuserprofile',
            name='plant_assignment',
            field=models.CharField(blank=True, choices=[('National Office - Pasig', 'National Office - Pasig'), ('BMEG-Bataan 1', 'BMEG-Bataan 1'), ('BMEG-Bataan 2', 'BMEG-Bataan 2'), ('BMEG-Echague', 'BMEG-Echague'), ('BMEG-Leganes', 'BMEG-Leganes'), ('BMEG-Ormoc', 'BMEG-Ormoc'), ('BMEG-Pavia', 'BMEG-Pavia'), ('BMEG-San Ildefonso', 'BMEG-San Ildefonso'), ('BMEG-Sta. Cruz', 'BMEG-Sta. Cruz'), ('BMEG-Tagoloan', 'BMEG-Tagoloan'), ('BMEG-Tarlac', 'BMEG-Tarlac'), ('BMEG-Pangasinan', 'BMEG-Pangasinan'), ('Mills-Mabini 1', 'Mills-Mabini 1'), ('Mills-Mabini 2', 'Mills-Mabini 2'), ('Mills-Tabangao', 'Mills-Tabangao'), ('BMEG-Mandaue', 'BMEG-Mandaue'), ('Mills-Mabini Premix', 'Mills-Mabini Premix'), ('Monterey-Sumilao', 'Monterey-Sumilao')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='customuserprofile',
            name='position',
            field=models.CharField(blank=True, choices=[('Operations Analyst', 'Operations Analyst'), ('Material Custodian', 'Material Custodian'), ('Maintenance Planner', 'Maintenance Planner'), ('Supervisor', 'Supervisor'), ('Engineering Head', 'Engineering Head'), ('Area Engineering Head', 'Area Engineering Head'), ('National Operations Manager', 'National Operations Manager'), ('General Manager', 'General Manager')], max_length=100, null=True),
        ),
    ]
