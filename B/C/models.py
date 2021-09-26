from django.db import models
from django.db.models.fields import CharField

class Car(models.Model):
    car_name = models.CharField(max_length=200)
    car_price = models.FloatField()
    car_quantity = models.PositiveIntegerField()
    
