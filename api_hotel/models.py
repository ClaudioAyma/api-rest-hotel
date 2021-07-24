from django.db import models

class Habitacion(models.Model):
    numero_habitacion = models.IntegerField(unique=True)
    detalles_de_habitacion = models.CharField(max_length=200)
    capacidad = models.IntegerField(default=0)

    REQUIRED_FIELDS = ['numero_habitacion', 'detalles_de_habitacion', 'capacidad']

    def __str__(self) -> str:
        return f'Numero {self.numero_habitacion}'

class Cliente(models.Model):
    nombre = models.CharField(max_length=10)
    apellido = models.CharField(max_length=20)
    cedula_identidad = models.IntegerField()

    REQUIRED_FIELDS = ['nombre', 'appelido', 'cedula_identidad']

    def __str__(self) -> str:
        return f'{self.nombre} {self.apellido}'

class Reserva(models.Model):

    estados_de_reservacion = [
        ('PENDIENTE', 'PENDIENTE'),
        ('PAGADO', 'PAGADO'),
        ('ELIMINADO', 'ELIMINADO')
    ]
    metodos_de_pagos = [
        ('CONTADO', 'CONTADO'),
        ('TRANSACCION', 'TRANSACCION'),
        ('DEBITO', 'DEBITO')
    ]
    estado = models.CharField(max_length=9, choices=estados_de_reservacion)
    estadia_inicio = models.DateTimeField()
    estadia_final = models.DateTimeField()
    habitacion = models.ForeignKey(Habitacion, on_delete=models.CASCADE)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    metodo_de_pago = models.CharField(max_length=14, choices=metodos_de_pagos)
    monto = models.IntegerField()

    def __str__(self) -> str:
        return f"Cliente: {self.cliente.nombre} | Habitacion: {self.habitacion.numero_habitacion}"

    def facturacion(self) -> dict:
        # Si el estado de la reserva es pagado o eliminado entonces se puede
        # generar la factura y si no osea es PENDIENTE entonces se genera un mensaje
        # de que aun no se genero la factura.
        if self.estado in ('PAGADO', 'ELIMINADO'):
            factura = {
                'cliente': f'{self.cliente.nombre} {self.cliente.apellido}',
                'habitacion': f'{self.habitacion.numero_habitacion}',
                'detalles_habitacion': f'{self.habitacion.detalles_de_habitacion}',
                'metodo_pago': f'{self.metodo_de_pago}',
                'monto' : f'{self.monto}'
            }
        else :
            factura = {
                'mensaje': 'Factura no generada porque el cliente aun no ha pagado la reservacion'
            }

        return factura