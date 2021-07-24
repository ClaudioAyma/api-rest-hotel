from api_hotel.models import Reserva, Habitacion

# Eesta funcion verifica si la habitacion evaluada esta disponible
# en el rango de tiempo de inicio y final.
def verificar_disponibilidad(habitacion, inicio, final) -> bool:    
    disponibilidad = []
    lista_de_reservas = Reserva.objects.filter(habitacion=habitacion)

    for _reserva in lista_de_reservas:
        if _reserva.estadia_inicio > final or _reserva.estadia_final < inicio:
            disponibilidad.append(True)
        else:
            disponibilidad.append(False)
    
    return all(disponibilidad)  
