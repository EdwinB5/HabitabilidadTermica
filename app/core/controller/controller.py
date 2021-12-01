from .operaciones import calcular_habitaciones
from ..model.edificio import Edificio
from ..model.habitacion import Habitacion
import re
from random import choice, randrange

class Controller:
	'''
	Esta clase hace de mediador entre los modelos y la vista
	'''
	def __init__(self, habitaciones_edificio:list = []):
		self.habitaciones_edificio = habitaciones_edificio
		self.edificio = Edificio()
		self.coeficiente = 0
		self.habitacion = Habitacion()
		self.edificio_completo = []

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
		self.habitacion_cantidad_alta = 0
		self.habitacion_cantidad_media = 0
		self.habitacion_cantidad_baja = 0


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
		lista_aux = []
		num = 0
		for piso in self.habitaciones_edificio:
			if piso:
				lista_aux.append([])
			for habitacion in piso:
				if not habitacion.estado == False:
					lista_aux[num].append(habitacion)
			num += 1
		
		self.habitaciones_edificio = lista_aux
	
	def propagar_temperatura(self):
		'''
		Este método realiza la propagación a través del edificio
		'''
		for piso in self.habitaciones_edificio:
			for x ,habitacion in enumerate(piso):
				if x == 0:
					habitacion.temperatura = self.edificio.calcular_temperatura_habitacion(habitacion, self.edificio.temperatura, 10)
				else:
					habitacion_anterior = piso[x-1]
					habitacion_anterior_temperatura = habitacion.temperatura_inicial
					habitacion_anterior_coeficiente = habitacion.coeficiente_transferencia
					habitacion.temperatura = self.edificio.calcular_temperatura_habitacion(habitacion, habitacion_anterior_temperatura, habitacion_anterior_coeficiente)

	def calcular_humedad_edificio(self):
		'''
		Esta función calcula la humedad en el edificio, es relevante
		dado que utiliza la estación de año
		'''
		
		humedades = []
		for piso in self.habitaciones_edificio:
			for habitacion in piso:
				humedad_habitacion = habitacion.humedad
				humedad_habitacion = re.sub('%','', humedad_habitacion)
				humedades.append(float(humedad_habitacion)/100)
		
		humedad_edificio = 0.0
		for humedad in humedades:
			humedad_edificio += humedad

		return humedad_edificio/len(humedades)

	def calcular_habitabilidad(self):
		'''

		---ALTA----
		12-27 TEMPERATURA
		15 - 60 HUMEDAD
		---MEDIA---
		0-12 & 27-36 Temperatura
		15-10 & 60-85  Humedad
		---BAJA---
		0< & 36> Temperatura
		10< & 85> Humedad
		
  
		'''
		habitacion_alta = ['']
		habitacion_media = ['']
		habitacion_baja = ['']

		for piso in self.habitaciones_edificio:
			for habitacion in piso:
				if float(habitacion.temperatura) >= 12 and float(habitacion.temperatura) <= 27:
					habitacion.habitabilidad = 'Alta'
					habitacion_alta.append(habitacion)
				elif float(habitacion.temperatura) >= 0 and float(habitacion.temperatura) <= 12 or float(habitacion.temperatura) >= 27 and float(habitacion.temperatura) <= 36:
					habitacion.habitabilidad = 'Media'
					habitacion_media.append(habitacion)
				elif float(habitacion.temperatura) < 0 or float(habitacion.temperatura) > 36:
					habitacion.habitabilidad = 'Baja'
					habitacion_baja.append(habitacion)
				else:
					habitacion.habitabilidad = 'Nula'

		if len(habitacion_alta) > len(habitacion_media) and len(habitacion_alta) > len(habitacion_baja):
			self.edificio.habitabilidad_edificio = 'Alta'
		elif len(habitacion_media) > len(habitacion_alta) and len(habitacion_media) > len(habitacion_baja):
			self.edificio.habitabilidad_edificio = 'Media'
		elif len(habitacion_baja) > len(habitacion_alta) and len(habitacion_baja) > len(habitacion_media):
			self.edificio.habitabilidad_edificio = 'Baja'
		else:
			self.edificio.habitabilidad_edificio = choice(['Alta', 'Baja', 'Media'])
		
		self.habitacion_cantidad_alta = len(habitacion_alta)
		self.habitacion_cantidad_media = len(habitacion_media)
		self.habitacion_cantidad_baja = len(habitacion_baja)

	def calcular_nivel_confort(self):
		'''
		Este metodo permite calcular el nivel de confort

		75 - 100 ALTA
		45 - 74 MEDIA
		0 - 44 BAJA
		'''
		confort = 0
		color = 'success'

		if self.edificio.habitabilidad_edificio == 'Alta':
			confort = randrange(75, 100)
			color = 'success'
		elif self.edificio.habitabilidad_edificio == 'Media':
			confort = randrange(45, 74)
			color = 'warning'
		elif self.edificio.habitabilidad_edificio == 'Baja':
			confort = randrange(0, 44)
			color = 'danger'
		
		return confort, color

	def calcular_area_edificio(self):
		'''
		Este metodo calcula el area del edificio
		'''
		return self.edificio.tamaño * self.edificio.tamaño

	def recuperar_datos_salida(self):
		'''
		Este metodo permite recuperar los datos de salida para la pantalla
		de salida del formulario
		'''
		try:
			area = self.calcular_area_edificio()
		except:
			area = 0
		temperatura_promedio = 0

		nivel, color = self.calcular_nivel_confort()
		habitaciones_habitables = 0
		habitaciones_no_habitables = 0
		try:
			habitacion_alta = self.habitacion_cantidad_alta
			habitacion_media = self.habitacion_cantidad_media
			habitacion_baja = self.habitacion_cantidad_baja
		except:
			habitacion_alta = 0
			habitacion_media = 0
			habitacion_baja = 0

		pisos = len(self.edificio_completo)
		#humedad_edificio = float(self.edificio.humedad)
		humedad_edificio = 0
		datos_salida = {
			'habitabilidad': self.edificio.habitabilidad_edificio,
			'area_total': area,
			'humedad': humedad_edificio,
			'temperatura_promedio': temperatura_promedio,
			'nivel_confort': nivel,
			'color_alerta': color,
			'habitaciones_habitables': habitaciones_habitables,
			'habitaciones_no_habitables': habitaciones_no_habitables,
			'habitacion_alta': habitacion_alta,
			'habitacion_media': habitacion_media,
			'habitacion_baja': habitacion_baja,
			'pisos': pisos
		}

		return datos_salida

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
		self.propagar_temperatura()
		#self.calcular_habitabilidad()
		humedades = self.calcular_humedad_edificio()
		self.edificio.humedad = f'{humedades*100}%'
		self.calcular_habitabilidad()
		print('Edificio completo')
		self.imprimir_habitaciones_edificio()
		self.edificio_completo = self.habitaciones_edificio
		self.eliminar_habitaciones_sin_uso()
		print('Edificio depurado')
		self.imprimir_habitaciones_edificio()