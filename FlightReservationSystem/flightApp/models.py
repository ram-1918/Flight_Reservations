from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.conf import settings

# Create your models here.

class Flight(models.Model):
    flightNumber = models.CharField(max_length = 20) # Why can't this be a primary key?
    operatingAirlines = models.CharField(max_length=20)
    departureCity = models.CharField(max_length = 20)
    arrivalCity = models.CharField(max_length = 20)
    dateOfDeparture = models.DateField()
    estimatedTimeOfDeparture = models.TimeField()

    class Meta:
        verbose_name_plural = "Flights"

    def __str__(self):
        return self.operatingAirlines + ' (' + self.flightNumber + ') ' + ' from ' + self.departureCity + ' to ' + self.arrivalCity + ' on ' + str(self.dateOfDeparture)

class Passenger(models.Model):
    firstname = models.CharField(max_length = 20)
    lastname = models.CharField(max_length = 20)
    middlename = models.CharField(max_length = 20, blank = True, null = True)
    email = models.CharField(max_length= 40) #primary_key=True; EmailField?
    phone = models.CharField(max_length=10)

    class Meta:
        verbose_name_plural = "Passengers"
    
    def __str__(self):
        return self.firstname + ' ' + self.middlename + ' ' + self.lastname

class Reservation(models.Model):
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE)
    passenger = models.ForeignKey(Passenger, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Reservations"

@receiver(post_save, sender = settings.AUTH_USER_MODEL)
def CreateAuthToken(sender, instance, created, **kwargs):
    if created:
        Token.objects.create(user = instance)