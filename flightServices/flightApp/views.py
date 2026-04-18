from django.shortcuts import render
from rest_framework.response import Response   
from flightApp.models import Flight, Passenger, Reservation
from flightApp.serialzers import FlightSerializer, PassengerSerializer, ReservationSerializer 
from rest_framework import  viewsets
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework import filters
from rest_framework.permissions import IsAuthenticated
from rest_framework import permissions

# Create your views here.

@api_view(['POST'])
def findFlights(request):
    departureCity = request.GET.get('departureCity')
    arrivalCity = request.GET.get('arrivalCity')
    dateOfDeparture = request.GET.get('dateOfDeparture')

    flights = Flight.objects.filter(departureCity=departureCity, arrivalCity=arrivalCity, dateOfDeparture=dateOfDeparture)
    serializer = FlightSerializer(flights, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def save_reservation(request):
    flight = Flight.objects.get(id=request.data['flightId'])
    
    passenger = Passenger()
    passenger.firstName = request.data['firstName']
    passenger.lastName = request.data['lastName']
    passenger.middleName = request.data.get('middleName', '')
    passenger.email = request.data['email']
    passenger.phone = request.data['phone']
    passenger.save()

    reservation = Reservation()
    reservation.flight = flight
    reservation.passenger = passenger
    reservation.save()

    return Response(status= status.HTTP_201_CREATED, data={'message': 'Reservation saved successfully'})


class FlightViewSet(viewsets.ModelViewSet):
    queryset = Flight.objects.all()
    serializer_class = FlightSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['departureCity', 'arrivalCity', 'dateOfDeparture']
    permission_classes = [permissions.IsAuthenticated]

class PassengerViewSet(viewsets.ModelViewSet):
    queryset = Passenger.objects.all()
    serializer_class = PassengerSerializer

class ReservationViewSet(viewsets.ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer