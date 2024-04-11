from django.db import models

# Create your models here.

class Portfolio(models.Model):
    image = models.ImageField(upload_to="images/")
    filter = models.CharField(max_length=15, null=True,blank=True)