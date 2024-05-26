from django.db import models

# Create your models here.
class Car(models.Model):
    class Meta:
        db_table = 'car'

    vin = models.CharField(max_length=50)
    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    fuel = models.CharField(max_length= 50)
    power = models.PositiveIntegerField()
    horse_power = models.PositiveIntegerField()
    plate = models.CharField(max_length=50)

class Maintenance(models.Model):
    class Meta:
        db_table = 'maintenance'

    class Type(models.IntegerChoices):
        SERVICE = 1
        REPAIRS = 2

    type = models.IntegerField(choices=Type.choices)
    created_at = models.DateField(auto_now_add=True, auto_now=False, blank=True)
    mileage = models.IntegerField(blank=True, null=True)
    car_id = models.ForeignKey(Car, on_delete=models.CASCADE, null=True, blank=True, related_name='maintenance', db_column="car_id")

    # For example, if a Car model has a Maintenance – that is, a Maintenance makes multiple cars but each Car only has one Maintenance – use the following definitions:
    
class Service(models.Model):
    class Meta:
        db_table = 'service'
    
    class ServiceType(models.IntegerChoices):
        CHANGE = 1
        CHECK = 2

    service_type = models.IntegerField(choices = ServiceType.choices)
    title = models.CharField(max_length=150)
    description = models.TextField(blank=True, null=True)
    maintenance_id = models.ForeignKey(Maintenance, on_delete= models.CASCADE, null=True, blank = True, related_name='service', db_column="maintenance_id")
