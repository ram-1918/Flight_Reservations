from django.contrib import admin
from flightApp.models import Flight, Passenger, Reservation
# Register your models here.

class flightAdmin:
    list_display = ['flightNumber', 'operatingAirlines']
class passengerAdmin:
    list_display = ['firstname', 'lastname']
class reservationAdmin(admin.ModelAdmin):
    list_display = ['passenger', 'flight']

admin.site.register(Flight)
admin.site.register(Passenger)
admin.site.register(Reservation, reservationAdmin)