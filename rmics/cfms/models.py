from django.db import models

# Create your models here.


class FindingsLog(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    time_of_discovery = models.DateTimeField(max_length=100, blank=True, null=True)
    reported_time = models.DateTimeField(max_length=100, blank=True, null=True)
    findings_title = models.CharField(max_length=100, blank=True, null=True)
    findings_description = models.TextField(max_length=700, blank=True, null=True)
    action_plan = models.TextField(max_length=1000, blank=True, null=True)
    action_plan_schedule = models.DateTimeField(blank=True, null=True)
    parts_availability = models.CharField(max_length=200, choices=[('YES','Yes'), ('NO','No')], blank=True, null=True)
    status = models.CharField(max_length=20, choices=[('scheduled', 'Scheduled'), ('on-going', 'On-going repair'), ('waiting', 'Waiting for parts'), ('done', 'Done')], blank=True, null=True)
    comments = models.TextField(max_length=500, blank=True, null=True)

    def __str__(self):
        return self.findings_title