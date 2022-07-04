from django.db import models

# Create your models here.

class Vehicle(models.Model):
    name = models.CharField(db_index=True, max_length=255)
    brand = models.CharField(max_length=255)
    kilometers = models.IntegerField()
    last_oil_check = models.DateTimeField()

