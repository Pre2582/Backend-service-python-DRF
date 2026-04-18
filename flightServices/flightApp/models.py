from django.db import models

from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.conf import settings

# Create your models here.

class Flight(models.Model):
    flightNumber = models.CharField(max_length=100)
    operatingAirlines = models.CharField(max_length=100)
    # operatingAirlines = models.CharField(max_length=100 , blank=True, null=True)
    departureCity = models.CharField(max_length=100)
    arrivalCity = models.CharField(max_length=100)
    dateOfDeparture = models.DateTimeField()
    estimatedTimeOfDeparture = models.DateTimeField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.flightNumber

class Passenger(models.Model):
    firstName = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    middleName = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField()
    phone = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.firstName} {self.lastName}"

class Reservation(models.Model):
    # flight = models.OneToOneField(Flight, on_delete=models.CASCADE)
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE)
    passenger = models.OneToOneField(Passenger, on_delete=models.CASCADE)
    dateOfReservation = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Reservation for {self.passenger} on flight {self.flight}"    
    
@receiver(post_save, sender=settings.AUTH_USER_MODEL)  
def createAuthToken(sender, instance, created, **kwargs):
    if created:
        Token.objects.create(user=instance)    

# post_save.connect(createAuthToken, sender=settings.AUTH_USER_MODEL)