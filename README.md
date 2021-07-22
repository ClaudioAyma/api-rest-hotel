## API Rest para sistema de reservacion en Hotel

### Requerimientos y condiciones:

- Las reservas pueden tener 3 estados: Pendiente, Pagado y Eliminado.
- Los datos a almacenar para la reserva son: los detalles del cuarto reservado, los días de estadía, los datos de facturación e identificación del cliente, el monto pagado y el método de pago.

### Planteamiento del proyecto
Un sistema de reservacion maneja algunos modelos como ``Cliente`` y ``Habitacion``  que se relacionan para crear una ``Reserva`` de acuerdo a esta ultima clase se puede aplicar mucha logica ya sea para la reservacion, facturacion, etc.

### Caracteristicas del proyecto
- El proyecto debe ser capaz de registrar habitaciones y clientes ya que sin estos campos no se podria crear una reserva.
- Debe poder registrar reservas asociando 1 cliente por cada habitacion.
- Debe poder devolver la informacion tanto de clientes, habitaciones y reservas
- 

### Planteamiento del desarrollo
Al tratarse de un sistema de reservacion que puede incluir muchas funcionabilidades que se pueden ir implementando a lo largo del tiempo decidi modularlo y crear una app en django llamada ``api_hotel``  que tiene la siguiente estructura de archivos en los cuales he trabajado :
```
api_hotel:
	admin.py
	models.py
	serializer.py
	urls.py
	views.py
```

### Modelado

##### HABITACION
Una habitacion tiene numero de habitacion, detalles y la capacidad de personas.
```python
class  Habitacion(models.Model):

numero_habitacion = models.IntegerField(unique=True)
detalles_de_habitacion = models.CharField(max_length=200)
capacidad = models.IntegerField(default=0)
```
##### CLIENTE
Un cliente tiene nombre, apellido y la cedula de identidad.
```python
class  Cliente(models.Model):

nombre = models.CharField(max_length=10)
apellido = models.CharField(max_length=20)
cedula_identidad = models.IntegerField()
```
##### RESERVA
En este modelo relaciono los anteriores dos ya que una reserva incluye habitacion y cliente. Ademas en estadia decidi utilizar dos atributos tanto para la entrada al hotel ``estadia_inicio`` y salida ``estadia_final`` esto facilita al proyecto al momento de implementar logica de verificacion si una habitacion esta disponible o no.

En los atributos ``estado`` y ``metodo_de_pago`` los configure solo para que reciban categorias (no se ve en el codigo de abajo ya que es un simple resumen de lo que esta en el proyecto)
```python
class  Reserva(models.Model):

	estado = models.CharField()
	estadia_inicio = models.DateTimeField()
	estadia_final = models.DateTimeField()
	habitacion = models.ForeignKey(Habitacion)
	cliente = models.ForeignKey(Cliente)
	metodo_de_pago = models.CharField()
	monto = models.IntegerField()
	
	def  facturacion(self):	
		factura = f"""
		Cliente : {self.cliente.nombre} + {self.cliente.apellido}
		Habitacion : {self.habitacion.numero_habitacion}
		Detalles de la habitacion: {self.habitacion.detalles_de_habitacion}
		Metodo de pago: {self.metodo_de_pago}
		Monto : {self.monto}
		"""
		return  factura
```
La funcion ``facturacion``  como un metodo de la clase ``reserva ``que devuelve un string con la informacion necesaria para una factura.

##  Tutorial
Usamos el metodo ``GET`` para obtener todos los datos
y para registrarlos utilizamos el metodo ``POST`` en la misma direccion.

1. Para clientes
``localhost:8000/api-hotel/clientes/``

2. Para habitaciones
``localhost:8000/api-hotel/habitaciones/``

3. Para reservas
``localhost:8000/api-hotel/reservas/``

## Limitaciones

Al tratarse de un proyecto rapido y con pocos requerimientos tiene muchas limitaciones y funcionabilidades no agregadas como:

- No se puede actualizar habitaciones, clientes y reservas, solo registrar y obtener.
- Se pueden crear reservas repetidas porque no se creo una funcion para verificar la disponibilidad de las habitaciones.


