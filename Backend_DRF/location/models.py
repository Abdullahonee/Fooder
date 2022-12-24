from django.db import models

# Create your models here.
class LocationDist(models.Model):
    start = models.CharField(max_length = 100)
    end = models.CharField(max_length = 100)
    distance = models.DecimalField(default=0, max_digits=15, decimal_places=10)
    
class Locations(models.Model):
    name = models.CharField(max_length=100, unique=True)
    
    def __str__(self):
        return self.name;