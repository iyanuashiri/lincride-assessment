from decimal import Decimal

from django.db import models

# Create your models here.


class Driver(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    
    
class Rider(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)

 
class Ride(models.Model):
    TRAFFIC_LEVEL = [
        ("low", Decimal('1.0')),
        ("normal", Decimal('1.2')),
        ("high", Decimal('1.5')),
        
    ]
    
    DEMAND_LEVEL = [
        ("normal", Decimal('1.0')),
        ("peak", Decimal('1.8')),
    ]
    # There would probably been a driver and a rider fields, but because of the specific tasks in the project, I didnt use them. 
    # driver = models.ForeignKey(Driver, on_delete=models.CASCADE, related_name="driver_rides")
    # rider = models.ForeignKey(Rider, on_delete=models.CASCADE, related_name="rider_rides")
    
    distance = models.DecimalField(max_digits=19, decimal_places=8)
    traffic_level = models.CharField(choices=TRAFFIC_LEVEL, max_length=10)
    demand_level = models.CharField(choices=DEMAND_LEVEL, max_length=10)
    
    traffic_multiplier = models.DecimalField(max_digits=19, decimal_places=2)
    demand_multiplier = models.DecimalField(max_digits=19, decimal_places=2)
    time_multiplier = models.DecimalField(max_digits=3, decimal_places=1)
    distance_fare = models.DecimalField(max_digits=19, decimal_places=2, default=Decimal('0.00'))
    total_fare = models.DecimalField(max_digits=19, decimal_places=2, default=Decimal('0.00'))
    
    
    
