from .operaciones import calcular_habitaciones
from ..model.edificio import Edificio
from ..model.habitacion import Habitacion
class Controller:
	'''
	Esta clase hace de mediador entre los modelos y la vista
	'''
	def __init__(self, habitaciones_edificio:list = []):
		self.habitaciones_edificio = habitaciones_edificio
		self.edificio = Edificio()
		self.coeficiente = 0
		self.habitacion = Habitacion()

	def cargar_datos_edificio(self, estacion, humedad, temperatura_ambiente, tamaño_edificacion):
		'''
		'''
		self.edificio.temperatura = temperatura_ambiente
		self.edificio.estacion = estacion
		self.edificio.humedad = humedad
		self.edificio.tamaño = tamaño_edificacion
		self.edificio.dimensiones = (tamaño_edificacion, tamaño_edificacion)

	def datos_controller(self, estacion, humedad, temperatura_ambiente, tamaño_edificacion, coeficiente):
		'''
		Esta función conecta la entrada de datos con
		los modelos
		'''
		self.coeficiente = coeficiente

		self.cargar_datos_edificio(estacion, humedad, temperatura_ambiente, tamaño_edificacion)
		self.habitaciones_edificio = calcular_habitaciones(self.edificio.dimensiones, self.habitacion.dimensiones)
		self.edificio.pisos = len(self.habitaciones_edificio)
	