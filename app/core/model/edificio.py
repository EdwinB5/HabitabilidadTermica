class Edificio:
	'''
	Esta clase representa el edificio con sus
	respectivos valores iniciales, también contiene
	las funciones para la propagación del fenomeno
	'''
	def __init__(self, temperatura:int = 0, estacion:str = 'Ninguna', tamaño:int = 0, humedad:int = 0, pisos:int = 0):
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
		self.dimensiones = (0, 0)
		self.humedad = humedad
		self.pisos = pisos
		self.habitabilidad_edificio = 'Ninguna'

	def __str__(self):
		'''
		Esta función permite leer la clase a manera de cadena
		'''
		return f'Edificio: [(Temperatura: {self.temperatura}), (Estación: {self.estacion}), (Tamaño: {self.tamaño}), (Dimensiones: {self.dimensiones}), (Humedad: {self.humedad}), (Pisos: {self.pisos})), (Habitabilidad: {self.habitabilidad_edificio})]'

	
	def calcular_temperatura_habitacion(self, habitacion, temperatura_habitacion_anterior, coeficiente_transferencia_anterior):
		'''
		Esta función se utiliza para calcular la temperatura
		en una habitacion concreta, teniendo en cuenta los cambios

		:param habitacion: la habitacion que será medida su temperatura
		:type habitacion: Habitacion<Object>
		:param temperatura_habitacion_anterior: la temperatura de la habitacion anterior
		:type temperatura_habitacion_anterior: int
		:param coeficiente_transferencia_anterior: el coeficiente de la habitacion anterior
		:type coeficiente_transferencia_anterior: int
		:returns: La temperatura que se propaga en esa habitacion
		:rtype: float
		'''
		densidad_pared = 0.15
		coeficiente_transferencia_1 = habitacion.coeficiente_transferencia
		coeficiente_transferencia_2 = coeficiente_transferencia_anterior
		conductividad_material = 1
		temperatura_1 = temperatura_habitacion_anterior
		temperatura_2 = habitacion.temperatura
		habitacion.resistencia = 1/((1/float(coeficiente_transferencia_1))+(float(densidad_pared)/float(conductividad_material))+(1/float(coeficiente_transferencia_2)))
		resistencia = habitacion.resistencia

		operacion_temperatura_propagada = (float(temperatura_1)-float(temperatura_2))*float(resistencia)

		
		temperatura_propagada = float(operacion_temperatura_propagada)/float(resistencia)
		#humedad = self.calcular_humedad_edificio(habitacion.humedad)
		
		return float(temperatura_propagada)