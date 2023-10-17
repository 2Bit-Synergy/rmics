from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models



class MaintenanceLog(models.Model):
    wo_seq_num = models.PositiveIntegerField(validators=[MinValueValidator(1, message="WORK SEQ NUM must be a positive number")], blank=True, null=True)
    machine_failure_breakdown = models.CharField(max_length=255, blank=True, null=True)
    description_of_work = models.TextField(max_length=600, blank=True, null=True)
    work_type = models.CharField(max_length=50, choices=[('Repair', 'Repair'), ('Preventive Maintenance', 'Preventive Maintenance'), ('Fabrication', 'Fabrication'), ('Equipment Setup', 'Equipment Setup'), ('General Jobs', 'General Jobs')], blank=True, null=True)
    root_cause = models.TextField(max_length=600, blank=True, null=True)
    job_start = models.DateTimeField(blank=True, null=True)
    job_end = models.DateTimeField(blank=True, null=True)
    time_consumed = models.TimeField(blank=True, null=True)
    affecting_production = models.TimeField(blank=True, null=True)
    affecting_time = models.TimeField(blank=True, null=True)
    equipment_name = models.CharField(max_length=255, blank=True, null=True)
    equipment_code = models.CharField(max_length=255, blank=True, null=True)
    section = models.CharField(max_length=255, blank=True, null=True)
    system = models.CharField(max_length=100, choices=[('Process', 'Process'), ('Civil', 'Civil'), ('Auxiliary', 'Auxiliary'), ('Plant Water', 'Plant Water'), ('Power', 'Power'), ('Steam', 'Steam'), ('Compressed Air', 'Compressed Air'), ('FFW', 'FFW')], default='Process', blank=True, null=True)
    affecting_bagging = models.BooleanField(blank=True, null=True)
    machine_failure = models.BooleanField(blank=True, null=True)
    type_of_stop_time = models.CharField(max_length=20, choices=[('Planned', 'Planned'), ('Unplanned', 'Unplanned')], blank=True, null=True)
    work_center = models.CharField(max_length=100, choices=[('Mechanical', 'Mechanical'), ('Electrical', 'Electrical'), ('Instrumentation & Controls', 'Instrumentation & Controls'), ('Fabrication', 'Fabrication'), ('Lubrication', 'Lubrication')], blank=True, null=True)
    personnel_assigned = models.CharField(max_length=255, blank=True, null=True)
    parts_replaced = models.CharField(max_length=255, blank=True, null=True)
    quantity_of_parts = models.IntegerField(blank=True, null=True)
    status = models.CharField(max_length=20, choices=[('Waiting for Parts', 'Waiting for Parts'), ('On-going', 'On-going'), ('Completed', 'Completed'), ('Pending', 'Pending')], blank=True, null=True)
    remarks = models.TextField(blank=True, null=True)
    spare_details = models.TextField(blank=True, null=True)
    notification_num = models.CharField(max_length=255, blank=True, null=True)
    include_log = models.BooleanField(default=True, blank=True, null=True)