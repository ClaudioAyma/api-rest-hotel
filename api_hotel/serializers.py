
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
            'id',
            'nombre',
            'apellido',
            'cedula_identidad'
        ]

class reservaGetSerializer(serializers.ModelSerializer):

    cliente = serializers.StringRelatedField()
    habitacion = serializers.StringRelatedField()
    
    class Meta:
        model = Reserva
        fields = [
            'id',
            'estado',
            'habitacion',
            'cliente',
            'estadia_inicio',
            'estadia_final',
            'metodo_de_pago',
            'monto',
        ]

class reservaSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Reserva
        fields = [
            'id',
            'estado',
            'habitacion',
            'cliente',
            'estadia_inicio',
            'estadia_final',
            'metodo_de_pago',
            'monto',
        ]

