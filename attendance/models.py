from django.db import models

# Create your models here.

class Attendant(models.Model):
    name = models.CharField(max_length=200)
    department = models.CharField(max_length=200)
    level = models.IntegerField()
    contact = models.CharField(max_length=200)

