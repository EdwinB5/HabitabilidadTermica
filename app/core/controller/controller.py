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
		Este metodo carga los datos digitados por el usuario al objeto edificio
		
		:param estacion: la estacion del edificio
		:type estacion: str
		:param humedad: la humedad presente en el edificio
		:type humedad: int, float
		:param temperatura_ambiente: la temperatura ambiente en el edificio
		:type temperatura_ambiente: int
		:param tamaño_edificio: el tamaño del edificio
		:type tamaño_edificio: ints
		'''
		self.edificio.temperatura = temperatura_ambiente
		self.edificio.estacion = estacion
		self.edificio.humedad = humedad
		self.edificio.tamaño = tamaño_edificacion
		self.edificio.dimensiones = (tamaño_edificacion, tamaño_edificacion)

	def imprimir_habitaciones_edificio(self):
		'''
		Este metodo permite imprimir el edificio y las habitaciones generadas en el
		'''
		print(self.edificio)

		for piso in self.habitaciones_edificio:
			for habitacion in piso:
				print(habitacion.__str__())
	
	def eliminar_habitaciones_sin_uso(self):
		'''
		Este metodo elimina las habitaciones del edificio que se encuentran sin uso
		'''
		for piso in self.habitaciones_edificio:
			for x, habitacion in enumerate(piso):
				if habitacion.estado == False:
					piso.pop(x)


	def main_controller(self, estacion, humedad, temperatura_ambiente, tamaño_edificacion, coeficiente):
		'''
		Este metodo conecta la entrada de datos con los modelos y
		la logica del proyecto

		:param estacion: la estacion que se encuentra el edificio
		:type estacion: str
		:param humedad: la humedad presentada en la temporada
		:type humedad: int
		:param temperatura_ambiente: la temperatura del ambiente
		:type temperatura_ambiente: int
		:param tamaño_edificio: el tamaño del edificio
		:type tamaño_edificio: int
		:param coeficiente: el coeficiente del material
		:type coeficiente: int, float
		'''
		self.coeficiente = coeficiente

		self.cargar_datos_edificio(estacion, humedad, temperatura_ambiente, tamaño_edificacion)
		self.habitaciones_edificio = calcular_habitaciones(self.edificio.dimensiones, self.habitacion.dimensiones, self.edificio.estacion, self.coeficiente)
		self.edificio.pisos = len(self.habitaciones_edificio)

		self.imprimir_habitaciones_edificio()
		self.eliminar_habitaciones_sin_uso()
		print('-'*100)
		print('Depurando edificio...')
		print('-'*100)
		self.imprimir_habitaciones_edificio()
			