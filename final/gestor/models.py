from django.db import models

# Create your models here.

class Gestor(models.Model):
    nombre = models.CharField(max_length=25)
