
from rest_framework import serializers
from api_hotel.models import Cliente, Habitacion, Reserva


class habitacionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Habitacion
        fields = [
            'numero_habitacion',
            'detalles_de_habitacion',
            'capacidad'
        ]

class clienteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Cliente
        fields = [
            'nombre',
            'apellido',
            'cedula_identidad'
        ]

class reservaSerializer(serializers.ModelSerializer):

    # client = serializers.StringRelatedField()
    # room = serializers.StringRelatedField()
    
    class Meta:
        model = Reserva
        fields = [
            'estado',
            'habitacion',
            'cliente',
            'estadia_inicio',
            'estadia_final',
            'metodo_de_pago',
            'monto',
        ]
