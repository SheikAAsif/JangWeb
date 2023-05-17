from django.db import models


class contactEnquiry(models.Model):
    user_name = models.CharField(max_length=30)
    user_last_name = models.CharField(max_length=30)
    user_address = models.CharField(max_length=100)
    user_old_address = models.CharField(max_length=100)
    user_city = models.CharField(max_length=100)


# Create your models here.
