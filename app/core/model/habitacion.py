from .edificio import Edificio

class Habitacion(Edificio):
	'''
	Esta clase describe las habitaciones dentro del edificio,
	contiene todas las funciones necesarias para medir
	el fenomeno dentro de la habitación y como se propaga
	'''
	def __init__(self, num_habitacion:int = 0, temperatura:int = 0, dimensiones:tuple = (5, 5), coeficiente_transferencia:int = 0, resistencia:int = 0, humedad:str = '0%', temperatura_inicial:int = 0, estado:bool = False, piso:int = 1, habitabilidad:str = ''):
		'''
		Este es el constructor de la clase habitacion
		
		:param temperatura: la temperatura en la habitacion
		:type temperatura: int
		:param dimensiones: las dimensiones de la habitacion
		:type dimensiones: tuple
		:param coeficiente_transferencia: coeficiente de transferencia general
		:type coeficiente_transferencia: int
		:param humedad: la humedad presente en la habitacion
		:type humedad: int
		:param resistencia: la resistencia en los muros
		:type resistencia: int
		:param temperatura_inicial: la temperatura en la habitacion
		:type temperatura_inicial: int
		:param estado: si la habitacion esta en uso:
		:type estado: bool
		:param habilitabilidad: si la habitacion es habitable
		:type habitabilidad: bool
		'''
		self.numero_habitacion = num_habitacion
		self.temperatura = temperatura
		self.dimensiones = dimensiones
		self.coeficiente_transferencia = coeficiente_transferencia
		self.resistencia = resistencia
		self.humedad = humedad
		self.temperatura_inicial = temperatura_inicial
		self.estado = estado
		self.piso = piso
		self.habitabilidad = habitabilidad

	def __str__(self):
		'''
		Esta función permite leer a manera de cadena la habitacion
		'''
		return f'Habitacion: [(Número habitación:{self.numero_habitacion}), (Temperatura: {self.temperatura}), (Dimensiones: {self.dimensiones}), (Coeficiente: {self.coeficiente_transferencia}), (Resistencia: {self.resistencia}), (Temperatura habitación: {self.temperatura_inicial}), (Estado habitación: {self.estado}), (Piso: {self.piso}), (Humedad: {self.humedad}), (Habitabilidad: {self.habitabilidad})]'