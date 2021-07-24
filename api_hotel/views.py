from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import serializers, status

from .models import Habitacion, Cliente, Reserva

from api_hotel.serializers import habitacionSerializer, clienteSerializer, reservaGetSerializer, reservaSerializer

class habitacionView(APIView):
    """ Api de habitacion """

    serializer_class = habitacionSerializer

    def get(self, request, format=None):

        # Obteniendo todos los registros de la base de datos
        habitaciones = Habitacion.objects.all()
        # Serializando los registros
        serializer = self.serializer_class(habitaciones, many=True)

        return Response(serializer.data)

    def post(self, request):

        # Serializando los valores recibidos mediante post
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():

            # Si los datos son validos instanciamos un objeto de la clase habitacion
            # para luego guardar los registros en la base de datos
            serializer.save()
            return Response(serializer.data)
        else:
            # Si los datos no son validos mostramos el error en el serializer
            # y un error 400 de mala solicitud
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )


class clienteView(APIView):
    """ Api de cliente """

    serializer_class = clienteSerializer

    def get(self, request, format=None):

        # Obteniendo todos los registros de la base de datos
        clientes = Cliente.objects.all()
        # Serializando los registros
        serializer = self.serializer_class(clientes, many=True)

        return Response(serializer.data)

    def post(self, request):

        # Serializando los valores recibidos mediante post
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():

            # Si los datos son validos instanciamos un objeto de la clase habitacion
            # para luego guardar los registros en la base de datos
            serializer.save()

            return Response(serializer.data)
        else:
            # Si los datos no son validos mostramos el error en el serializer
            # y un error 400 de mala solicitud
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

class reservaView(APIView):
    """ Api de reserva """

    serializer_class = reservaSerializer
    serializer_class_get = reservaGetSerializer
    serializer_class_post = reservaSerializer


    def get(self, request, format=None):

        # Obteniendo todos los registros de la base de datos
        reservas = Reserva.objects.all()

        # Serializando los registros
        serializer = self.serializer_class_get(reservas, many=True)

        # Retornando los registros
        return Response(serializer.data)

    def post(self, request):

        # Serializando los valores recibidos mediante post
        serializer = self.serializer_class_post(data=request.data)

        if serializer.is_valid():

            # Si es valido se guarda en la BD
            serializer.save()

            # Devuelve el objeto que se envio
            return Response(serializer.data)
        else:
            # Si los datos no son validos mostramos el error en el serializer
            # y un error 400 de mala solicitud
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

