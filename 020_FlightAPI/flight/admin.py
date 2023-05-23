from django.contrib import admin

from .views import (
    Passenger, Flight,Reservation
)

admin.site.register(Passenger)
admin.site.register(Flight)
admin.site.register(Reservation)