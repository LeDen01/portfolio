from django.db import models

# Create your models here.

class Temoignage(models.Model):
    auteur = models.CharField(max_length=50)
    poste = models.CharField(max_length=50)
    description = models.TextField()
    image = models.ImageField(upload_to="images/")