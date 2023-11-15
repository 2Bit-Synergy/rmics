from django import forms
from .models import FindingsLog
from django.forms import DateTimeInput, Textarea, Select



class FindingsLogForm(forms.ModelForm):    
    class Meta:
        model = FindingsLog
        fields = [
            'time_of_discovery', 
            'reported_time', 
            'findings_title',
            'findings_description', 
            'action_plan',
            'action_plan_schedule',
            'parts_availability', 
            'status', 
            'comments'   
        ]
