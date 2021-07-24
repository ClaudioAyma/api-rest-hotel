from api_hotel.viewsets import ClienteViewset, HabitacionViewset, ReservaViewset
from rest_framework import routers


router = routers.DefaultRouter()
router.register('clientes', ClienteViewset)
router.register('habitaciones', HabitacionViewset)
router.register('reservas', ReservaViewset)