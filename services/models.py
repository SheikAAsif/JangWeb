from django.db import models


class services(models.Model):
    services_pic=models.CharField(max_length=50)
    servicew_title=models.CharField(max_length=50)
    services_des=models.TextField()
    services_links=models.CharField(max_length=100)
    services_mini_title=models.CharField(max_length=50)
    
# Create your models here.
