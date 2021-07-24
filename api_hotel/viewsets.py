# Modulos de django
from rest_framework import viewsets
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

# Modelos y serializer
from . import models
from . serializers import clienteSerializer, habitacionSerializer, reservaGetSerializer, reservaSerializer

# Modulo con funciones adicionales
from . funciones.disponibilidad import verificar_disponibilidad



class ClienteViewset(viewsets.ModelViewSet):
    """ CRUD para clientes """
    queryset = models.Cliente.objects.all()
    serializer_class = clienteSerializer

class HabitacionViewset(viewsets.ModelViewSet):
    """ CRUD para habitaciones """
    queryset = models.Habitacion.objects.all()
    serializer_class = habitacionSerializer

class ReservaViewset(viewsets.ModelViewSet):
    """ CRUD para Reservas """
    queryset = models.Reserva.objects.all()
    serializer_class = reservaSerializer

    # Esta es una pequena variacion del serializer de reserva
    # La diferencia es que solo lo utilizo para el GET osea para
    # obtener los datos pero con una variacion, en vez de mostrar el id
    # de los clientes y habitaciones, este muestra el nombre del cliente
    # y numero de habitacion, esto para facilitar la tarea mas al frontend
    serializer_class_get = reservaGetSerializer

    # GET
    def list(self, request):

        # Obteniendo todos los registros de la base de datos
        reservas = models.Reserva.objects.all()

        # Serializando los registros
        serializer = self.serializer_class_get(reservas, many=True)

        # Retornando los registros
        return Response(serializer.data)

    # POST
    def create(self, request):

        # Serializando los datos enviados mediante post
        serializer = self.get_serializer(data=request.data)
        # Verificando si los datos son validos si no, lanza un error
        serializer.is_valid(raise_exception=True)

        # Una vez los datos son validados se necesita extraer 3 valores
        # de los datos enviados por usuario antes de insertar en la base de datos
        inicio = serializer.validated_data.get("estadia_inicio")
        final = serializer.validated_data.get("estadia_final")
        id_habitacion = serializer.validated_data.get("habitacion").id

        # con estos 3 valores (estadia_inicio, estadia_final, id de la habitacion)
        # se pueden verificar si la habitacion esta o no disponible 
        if verificar_disponibilidad(id_habitacion, inicio, final):
            # si esta disponible entonces se procede a insertar
            serializer.save()
            return Response(serializer.data)
        else:
            # Y si no esta disponible devuelve un mensaje de error
            return Response({
                'mensage':'Error al guardar la reserva habitacion no esta disponible en este horario'
                })
    # PUT
    def update(self, request):

        # Serializando los datos enviados mediante post
        serializer = self.get_serializer(data=request.data)
        # Verificando si los datos son validos si no, lanza un error
        serializer.is_valid(raise_exception=True)

        # Al igual que en el metodo create al momento de actualizar
        # se necesita verificar la disponibilidad de la habitacion
        inicio = serializer.validated_data.get("estadia_inicio")
        final = serializer.validated_data.get("estadia_final")
        id_habitacion = serializer.validated_data.get("habitacion").id

        if verificar_disponibilidad(id_habitacion, inicio, final):
            serializer.save()
            return Response(serializer.data)
        else:
            return Response({
                'mensage':'Error al guardar la reserva habitacion no esta disponible en este horario'
                })


    # GET para un objeto
    def retrieve(self, request, pk=None):

        # Obteniendo todos las reservas
        queryset = models.Reserva.objects.all()
        # Filtrando la reserva mediando el pk
        reserva = get_object_or_404(queryset, pk=pk)        
        # Se genera la factura que devuelve un diccionario
        factura = reserva.facturacion()
        # Se serializa la reserva obtenida
        serializer = reservaSerializer(reserva)

        # Aqui hago una copia de los datos que devuelve el serializer
        # y los transformo en diccionario para poder luego modificar
        # el valor que quiero devolver, en este caso quiero anadir el
        # campo factura para poder devolver con el response
        serializer_data = dict(serializer.data)
        serializer_data['factura'] = factura
        return Response(serializer_data)