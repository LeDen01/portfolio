from django.db import models

# Create your models here.

class Skills(models.Model):
    langage = models.CharField(max_length=100)
    level = models.IntegerField()
