from flightApp.models import Flight, Passenger, Reservation
from flightApp.serializers import FlightSerializer, PassengerSerializer, ReservationSerializer
from rest_framework import generics  
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
#from rest_framework import filters

# Function-Based View to find-flights Functionality
@api_view(['POST'])
def findFlights(request):
    #print(request.data['departureCity'])
    flights = Flight.objects.filter(departureCity = request.data['departureCity'], arrivalCity = request.data['arrivalCity'], dateOfDeparture = request.data['dateOfDeparture'])
    # Why serializer exactly and what are Response & request?
    serializer = FlightSerializer(flights, many = True)
    return Response(serializer.data, status = status.HTTP_200_OK) # Here the resulted serialized data is send back to the client as Response.

@api_view(['POST'])
def bookFlight(request):
    flight = Flight.objects.get(id = request.data['flightID'])
    passenger = Passenger()
    passenger.firstname = request.data['firstname']
    passenger.lastname = request.data['lastname']
    passenger.middlename = request.data['middlename']
    passenger.email = request.data['email']
    passenger.phone = request.data['phone']
    passenger.save() # Becaz of one-to-one/ many-to-one field, save the passenger data before passing it into reservation.passenger field.
    reservation = Reservation()
    reservation.flight = flight
    reservation.passenger = passenger
    reservation.save()
    return Response(status.HTTP_201_CREATED)


# Create views that perform basic CRUD operations.
# ---------- Flights class-based view using generics --------------
class FlightsList(generics.ListCreateAPIView):
    queryset = Flight.objects.all()
    serializer_class = FlightSerializer
    #filter_backends = [filters.SearchFilters]
    #search_fields = ['depatureCity', 'arrivalCity', 'dateOfDeparture#']
    permission_classes = [IsAuthenticated]

class AFlightDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Flight.objects.all()
    serializer_class = FlightSerializer
    permission_classes = [IsAuthenticated]

# ---------- Passenger class-based view using generics --------------
class PassengersList(generics.ListCreateAPIView):
    queryset = Passenger.objects.all()
    serializer_class = PassengerSerializer

class APassengerDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Passenger.objects.all()
    serializer_class = PassengerSerializer

# ------------ Reservation class-based view using generics -----------
class ReservationsList(generics.ListCreateAPIView):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer

class AReservationDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer

