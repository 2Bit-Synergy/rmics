from django.contrib import admin
from .models import FindingsLog



class FindingsLogAdmin(admin.ModelAdmin):
    list_display = (
        'time_of_discovery',
        'reported_time',
        'findings_title',
        'findings_description',
        'action_plan',
        'action_plan_schedule',
        'parts_availability',
        'status',
        'comments',
    )

admin.site.register(FindingsLog, FindingsLogAdmin)


# Register your models here.