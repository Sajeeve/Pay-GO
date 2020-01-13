from django.contrib import admin
from . models import Destinations,Includes,Booking, Contact
# Register your models here.

admin.site.register(Destinations)
admin.site.register(Includes)
admin.site.register(Booking)
admin.site.register(Contact)
