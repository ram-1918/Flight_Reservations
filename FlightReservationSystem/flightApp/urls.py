"""FlightReservationSystem URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, include
from flightApp import views
urlpatterns = [
    path('flights/', views.FlightsList.as_view()),
    path('flightdetails/<int:pk>', views.AFlightDetail.as_view()),
    path('passengers/', views.PassengersList.as_view()),
    path('passengerdetails/<int:pk>', views.APassengerDetail.as_view()),
    path('reservations/', views.ReservationsList.as_view()),
    path('reservationdetails/<int:pk>', views.AReservationDetail.as_view()),
    path('FindFlights/', views.findFlights),
    path('BookFlight/', views.bookFlight)
]
