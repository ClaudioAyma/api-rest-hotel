
## API Rest para sistema de reservacion en Hotel

  

### Requerimientos y condiciones:

  

- Las reservas pueden tener 3 estados: Pendiente, Pagado y Eliminado.

- Los datos a almacenar para la reserva son: los detalles del cuarto reservado, los días de estadía, los datos de facturación e identificación del cliente, el monto pagado y el método de pago.

  

### Planteamiento del proyecto

Un sistema de reservacion maneja algunos modelos como ``Cliente`` y ``Habitacion`` que se relacionan para crear una ``Reserva`` de acuerdo a esta ultima clase se puede aplicar mucha logica ya sea para la reservacion, facturacion, etc.

  

### Caracteristicas del proyecto

- El proyecto debe ser capaz de registrar habitaciones y clientes ya que sin estos campos no se podria crear una reserva.

- Debe poder registrar reservas asociando 1 cliente por cada habitacion.

- Debe poder devolver la informacion tanto de clientes, habitaciones y reservas

-

  

### Planteamiento del desarrollo

Al tratarse de un sistema de reservacion que puede incluir muchas funcionabilidades que se pueden ir implementando a lo largo del tiempo decidi modularlo y crear una app en django llamada ``api_hotel`` que tiene la siguiente estructura de archivos en los cuales he trabajado :

```

api_hotel:

	admin.py

	models.py

	serializers.py

	viewsets.py

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

```

 

## Tutorial

Usamos el metodo ``GET`` para obtener todos los datos

y para registrarlos utilizamos el metodo ``POST`` en la misma direccion.

  

1. Para clientes

``localhost:8000/api-hotel/clientes/``

  

2. Para habitaciones

``localhost:8000/api-hotel/habitaciones/``

  

3. Para reservas

``localhost:8000/api-hotel/reservas/``

  ## Mejoras
  - Se remplazaron las views por viewsets que manejan de manera mas facil las operaciones CRUD en especial para los modelos de Cliente y Habitacion.
  - Se creo un modulo ``funciones`` en el que se puede anadir funcionalidades que queremos aplicar a alguna parte de nuestro proyecto.
  - Se creo una funcion para verificar la disponibilidad de una habitacion, ahora si se registra una habitacion que esta disponible entonces se almacena en la base de datos de lo contrario no se almacena ademas devuelve un mensaje que dice que la habitacion no se encuentra disponible en ese horario.
  - Se mejoro el metodo de facturacion.
  - Se implemento que al consultar una reservacion especifica esta tenga una factura o no dependiendo del estado de la reservacion.
  - Se mejoro el GET de los datos para las reservas, ahora en vez de mostrar el id de cliente o habitacion, muestra un string con el nombre o numero de habitacion.

## Flujo para un front-end

- Se puede crear una pagina donde hayan un formulario en el que se pueda registrar una habitacion consultando la siguiente ruta del proyecto ``/api-hotel/habitaciones/`` hacer peticiones GET, POST y  PUT, DELETE para la siguiente ruta``/api-hotel/habitaciones/id_reserva/`` 
- Creacion de otra pagina o seccion para que se registren las reservas y los clientes, en esta pagina incluyo ambas para evitar la perdida de tiempo en estar consultando diferentes paginas cuando lo que se necesita al momento de hacer una reservacion es registrar un cliente y la reserva lo mas rapido posible. En esta pagina se consumiria datos de ``/api-hotel/clientes/``  y ``/api-hotel/reservas/`` ademas de que al momento de registrar un cliente el servidor devuelve el json con los datos registrados incluyendo el ``id`` que nos servira para poder adjuntarlo a la reserva y asi facilmente registrar una reserva.

#### En resumen : 
Se crean las habitaciones en una pagina aparte.
Los clientes y reservaciones se registrarn en la misma pagina para ahorrar tiempo y usar el ``id`` del cliente registrado para adjuntar facilmente a la reserva.
