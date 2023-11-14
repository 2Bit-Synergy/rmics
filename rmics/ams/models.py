from django.db import models
from django.urls import reverse
from django.shortcuts import redirect, render
from django.http import request
from django.db.models import Q




# Create your models here.



class Asset(models.Model):
    
    def __str__(self):
        return self.asset_manufacturer
    
    
    asset_manufacturer = models.CharField(max_length = 100)
    asset_model = models.CharField(max_length = 100)
    asset_rated_capacity = models.CharField(default=0, max_length = 100)
    asset_type = models.CharField(max_length=50, blank=True)
    asset_sub_type = models.CharField(max_length=50, blank=True)
    asset_drive_details = models.CharField(max_length=50, blank=True)
    asset_year = models.CharField(max_length = 50, blank=True)
    asset_month = models.CharField(max_length = 50, blank=True)
    asset_image_primary = models.ImageField(upload_to='pics', default='D:\Legacy Projects\rmics\rmics\media\dphd_1.jpg')
    
    def get_absolute_url(self):
        return render(request, template_name='ams/asset-list.html')
    
    
    

class PlantAssignment(models.Model):
    plant = models.CharField(max_length=50, blank=True, null=True)
    plant_code = models.CharField(max_length=50, blank=True, null=True)