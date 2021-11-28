class Controller:
	'''
	Esta clase hace de mediador entre los modelos y la vista
	'''
	def __init__(self):
		pass

	def datos_controller(self, estacion, humedad, temperatura_ambiente, tamaño_edificacion, coeficiente):
		'''
		Esta función conecta la entrada de datos con
		los modelos
		'''
		print(estacion)
		print(humedad)
		print(temperatura_ambiente)
		print(coeficiente)
		print(tamaño_edificacion)