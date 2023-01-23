from flightApp.models import Flight, Passenger, Reservation
from rest_framework import serializers

class FlightSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flight
        fields = '__all__' #['flightNumber', 'operatingAirlines']
        

class PassengerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Passenger
        fields = '__all__'

class ReservationSerializer(serializers.ModelSerializer):
    # For onotoone, dont we need to define forgien keys here
    #flight = ...
    #passenger = ...
    class Meta:
        model = Reservation
        fields = '__all__'
