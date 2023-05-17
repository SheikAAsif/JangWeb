from django.db import models
from tinymce.models import HTMLField
from autoslug import AutoSlugField

class News(models.Model):
    new_title=models.CharField(max_length=100)
    new_desc=HTMLField()
    new_image=models.FileField(upload_to="New_image/",max_length=250,null=True,default=None)

    news_slug=AutoSlugField(populate_from='new_title',unique=True,null=True,default=None)
    




# Create your models here.
