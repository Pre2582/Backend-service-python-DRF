from rest_framework import serializers
from .models import Flight, Passenger, Reservation
import re

def isFlightNumberValid(flightNumber):
    print("Validating flight number:", flightNumber)

class FlightSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flight
        fields = '__all__'
        validators = [isFlightNumberValid]
        
    def validate_flightNumber(self, value):
        # if not value.startswith('FL'):
        #     raise serializers.ValidationError("Flight number must start with 'FL'")
        # return value    
        pattern = r'^[a-zA-Z0-9]*$'  # alphanumeric characters only
        if not re.match(pattern, value):
            raise serializers.ValidationError("Flight number must start with 'FL' followed by exactly 3 digits")
        return value
    
    def validate(self, data): 
        print("Validating flight data:", data)
        return data

class PassengerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Passenger
        fields = '__all__'

class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = '__all__'