from ..model.habitacion import Habitacion

def generar_habitacion(num_hab:int = 0):
    habitacion = Habitacion(num_habitacion=num_hab)

    return habitacion

def calcular_habitaciones(dimensiones_edificio, dimensiones_habitacion):
    '''
    Esta función calcula la cantidad de habitaciones del edificio
    '''

    lista_habitaciones = [[]]
    suma_x = 0
    edificio_x = int(dimensiones_edificio[0])
    piso = 0
    num_habitacion = 1

    while suma_x < edificio_x:
        if suma_x == 30:
            piso += 1
            edificio_x -= suma_x
            suma_x = 0
            lista_habitaciones.append([])

        if suma_x < 30 and suma_x >= 5:
            habitacion = generar_habitacion(num_habitacion)
            lista_habitaciones[piso].append(habitacion.__str__())
            num_habitacion += 1
            
        
        suma_x += int(dimensiones_habitacion[0])

    # (100, 100)
    # (5, 5)
    return lista_habitaciones