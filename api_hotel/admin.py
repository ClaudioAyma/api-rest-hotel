from django.contrib import admin

from api_hotel import models

# Register your models here.

admin.site.register(models.Habitacion)
admin.site.register(models.Cliente)
admin.site.register(models.Reserva)