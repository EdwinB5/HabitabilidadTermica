from .edificio import Edificio

class Habitacion(Edificio):
	'''
	Esta clase describe las habitaciones dentro del edificio,
	contiene todas las funciones necesarias para medir
	el fenomeno dentro de la habitación y como se propaga
	'''
	def __init__(self, num_habitacion:int = 0, temperatura:int = 0, dimensiones:tuple = (5, 5), coeficiente_transferencia:int = 0, resistencia:int = 0, temperatura_inicial:int = 0, estado:bool = False):
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
		:param temperatura_inicial: la temperatura en la habitacion
		:type temperatura_inicial: int
		:param estado: si la habitacion esta en uso:
		:type estado: bool
		'''
		self.numero_habitacion = num_habitacion
		self.temperatura = temperatura
		self.dimensiones = dimensiones
		self.coeficiente_transferencia = coeficiente_transferencia
		self.resistencia = resistencia
		self.temperatura_inicial = temperatura_inicial
		self.estado = estado

	def __str__(self):
		'''
		Esta función permite leer a manera de cadena la habitacion
		'''
		return f'Habitacion: [(Número habitación:{self.numero_habitacion}), (Temperatura: {self.temperatura}), (Dimensiones: {self.dimensiones}), (Coeficiente: {self.coeficiente_transferencia}), (Resistencia: {self.resistencia})]'