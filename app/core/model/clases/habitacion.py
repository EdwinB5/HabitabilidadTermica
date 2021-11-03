from edificio import Edificio

class Habitacion(Edificio):
	'''
	Esta clase describe las habitaciones dentro del edificio,
	contiene todas las funciones necesarias para medir
	el fenomeno dentro de la habitación y como se propaga
	'''
	def __init__(self, temperatura:int = 0, dimensiones:tuple = (0, 0), coeficiente_transferencia:int = 0, resistencia:int = 0):
		'''
		Este es el constructor de la clase habitacion
		
		:param temperatura: la temperatura en la habitacion
		:type temperatura: int
		:param dimensiones: las dimensiones de la habitacion
		:type dimensiones: tuple
		:param coeficiente_transferencia: coeficiente de transferencia general
		:type coeficiente_transferencia: int
		:param resistencia: la resistencia en los muros
		:type resistencia: int
		'''
		self.temperatura = temperatura
		self.dimensiones = dimensiones
		self.coeficiente_transferencia = coeficiente_transferencia
		self.resistencia = resistencia

	def __str__(self):
		'''
		Esta función permite leer a manera de cadena la habitacion
		'''
		return f'Habitacion: [(temperatura: {self.temperatura}), (dimensiones: {self.dimensiones}), (coeficiente: {self.coeficiente_transferencia}), (resistencia: {self.resistencia})]'