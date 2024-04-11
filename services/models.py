from django.db import models

# Create your models here.

class Service(models.Model):
    icone = models.CharField(max_length=100)
    title = models.CharField(max_length=50)
    description = models.TextField()