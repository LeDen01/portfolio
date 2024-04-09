from django.db import models

# Create your models here.

class Person(models.Model):
    image = models.ImageField(upload_to="images/")
    birthday = models.DateField()
    age = models.PositiveIntegerField()
    website = models.URLField(blank=True)
    degree = models.CharField(max_length=50)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    city = models.CharField(max_length=100)
    freelance = models.BooleanField()
