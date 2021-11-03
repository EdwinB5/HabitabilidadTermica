class Edificio:
	'''
	Esta clase representa el edificio con sus
	respectivos valores iniciales, también contiene
	las funciones para la propagación del fenomeno
	'''
	def __init__(self, temperatura:int = 0, estacion:str = 'Ninguna', tamaño:int = 0, humedad:int = 0):
		'''
		Constructor de la clase Edificio

		:param temperatura: la temperatura inicial del edificio
		:type temperatura: int
		:param estacion: la estacion del año del edificio
		:type estacion: str
		:param tamaño: el tamaño del edificio
		:type tamaño: int
		:param humedad: la humedad existente en el edificio
		:type humedad: int
		'''
		self.temperatura = temperatura
		self.estacion = estacion
		self.tamaño = tamaño
		self.humedad = humedad

	def __str__(self):
		'''
		Esta función permite leer la clase a manera de cadena
		'''
		return f'Edificio: [(Temperatura: {self.temperatura}), (Estación: {self.estacion}), (Tamaño: {self.tamaño})]'

	def calcular_humedad_edificio(self):
		'''
		Esta función calcula la humedad en el edificio, es relevante
		dado que utiliza la estación de año
		'''
		self.humedad = 0

	@staticmethod
	def calcular_dimension_habitacion():
		'''
		Esta función calcula las dimensiones de las habitaciones
		a partir del tamaño del edificio
		'''
	
	@staticmethod
	def calcular_temperatura_habitacion():
		'''
		Esta función se utiliza para calcular la temperatura
		en una habitacion concreta, teniendo en cuenta los cambios
		'''