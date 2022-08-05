from django.contrib import admin

# Register your models here.
from reservation.models import Reservation, Rental

admin.site.register(Reservation)
admin.site.register(Rental)
