from django.db import models

# Create your models here.

class Productos(models.Model):
    nombre = models.CharField(max_length=25)
    imagen = models.CharField(max_length=1000)
    precio = models.IntegerField()