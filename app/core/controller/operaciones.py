from ..model.habitacion import Habitacion
from random import randrange, choice

def generar_temperatura_habitacion(estacion:str = 'primavera'):
    '''
    Esta función genera la temperatura inicial de la habitación en base
    a la estación

    :param estacion: la estacion que se encuentra el edificio
    :type estacion: str
    :returns: temperatura de la estacion
    :rtype: int

    Primavera         
    -----------------  
    Maximo  33 grados                          
    Minima  19 grados
    Promedio 26 grados
    -----------------
    
    Verano
    ------------------
    Maximo 32 grados
    Minima 21 grados
    Promedio 28 grados
    
    Otoño
    Maximo 22 Grados
    Minima 15 Grados
    Promedio 18 Grados
    
    Invierno
    Maximo 22 Grados
    Minima 2 Grados
    Promedio 11 Grados
    
    '''
    temperatura_inicial = 0

    if estacion == 'primavera':
        temperatura_inicial = randrange(19, 33)
    elif estacion == 'verano':
        temperatura_inicial = randrange(28, 32)
    elif estacion == 'invierno':
        temperatura_inicial = randrange(2, 22)
    elif estacion == 'otoño':
        temperatura_inicial = randrange(18, 22)
    
    return temperatura_inicial
    
def uso_habitacion(num_hab:int = 0):
    '''
    Esta función asigna el estado de la habitacion si se encuentra en uso
    o no
    '''
    estado_habitacion = choice([True, False])
    
    return estado_habitacion

def generar_habitacion(num_hab:int = 0, estacion:str= 'primavera', coeficiente:int = 0, piso_habitacion:int = 0):
    '''
    Esta función genera las habitaciones en el edificio
    
    :param num_hab: este numero identifica la habitación
    :type num_hab: int
    :returns: retorna la habitacion
    :rtype: Habitacion<Object>
    '''
    # Generación atributos de habitaciones
    humedad_habitacion = calcular_humedad_habitacion(estacion)
    estado_habitacion = uso_habitacion(num_hab)
    temperatura_estacion = generar_temperatura_habitacion(estacion)
    habitacion = Habitacion(num_habitacion=num_hab, humedad=humedad_habitacion, temperatura_inicial=temperatura_estacion, estado=estado_habitacion, coeficiente_transferencia=coeficiente, piso=piso_habitacion)

    return habitacion

def calcular_humedad_habitacion(estacion):
    '''
    Esta función calcula la humedad en la habitacion, segun
    la estacion

    Primavera
  -------------  
    Minimo 78%
    Maximo 92%
    
    
    Verano
   ----------- 
    Minimo 18%
    Maximo 88%
    
    Otoño
    ---------------
    Minimo 20%
    Maximo 90%
    
    Invierno 
    -----------------
    Minimo 82%
    Maximo 96%    
    '''
    humedad = '0%'
    valor = 0

    if estacion == 'primavera':
        valor = randrange(78, 92)
        humedad = f'{valor}%'
    elif estacion == 'verano':
        valor = randrange(18, 88)
        humedad = f'{valor}%'
    elif estacion == 'otoño':
        valor = randrange(20, 90)
        humedad = f'{valor}%'
    elif estacion == 'invierno':
        valor = randrange(82, 96)
        humedad = f'{valor}%'
    
    return humedad


def calcular_habitaciones(dimensiones_edificio:tuple, dimensiones_habitacion:tuple, estacion:str, coeficiente:int):
    '''
    Esta función calcula la cantidad de habitaciones del edificio
    
    :param dimensiones_edificio: las dimensiones que tiene el edificio
    :type dimensiones_edificio: int
    :param dimensiones_habitacion: las dimensiones de las habitaciones
    :type dimensiones_habitacion: int
    :returns: lista de habitaciones en el edificio
    :rtype: list
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

        if suma_x < 30 and suma_x % 5 == 0:
            habitacion = generar_habitacion(num_habitacion, estacion, coeficiente, len(lista_habitaciones))
            lista_habitaciones[piso].append(habitacion)
            num_habitacion += 1  
        
        suma_x += int(dimensiones_habitacion[0])

    return lista_habitaciones