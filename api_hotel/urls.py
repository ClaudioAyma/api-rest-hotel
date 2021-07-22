from django.urls import path

from api_hotel import views

urlpatterns = [
    path('habitaciones/', views.habitacionView.as_view()),
    path('clientes/', views.clienteView.as_view()),
    path('reservas/', views.reservaView.as_view()),
]


