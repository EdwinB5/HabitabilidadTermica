from flask import Flask, render_template, request
from .controller import controller

app = Flask(__name__, template_folder='view', static_folder='view/static/')

@app.route('/', methods=['GET', 'POST'])
def datos_entrada():
	'''
	Vista principal del proyecto, formulario de entrada
	'''
	return render_template('index.html')

@app.before_request
def obtener_datos():
	'''
	Obteniendo datos del formulario y enviandolos al controlador
	para empezar la evaluacion de habitabilidad
	'''
	if request.method == 'POST':
		estacion = request.form.get('estacion')
		humedad = request.form.get('humedad')
		temperatura_ambiente = request.form.get('temperatura')
		tamaño_edificacion = request.form.get('tamaño')
		coeficiente = request.form.get('coeficiente')
		controller.datos_controller(estacion, humedad, temperatura_ambiente, tamaño_edificacion, coeficiente)

@app.route('/salida', methods=['GET', 'POST'])
def datos_salida():
	'''
	Vista salida del proyecto, plantilla salida
	'''

	return render_template('resultado.html')

# Web services

def run(host, port):
	'''
	Esta función pone a correr la aplicación flask

	:param host: esta es la dirección en la que se aloja la aplicación
	:type host: str
	:param port: el puerto donde se aloja la aplicación
	:type port: int
	'''
	app.run(host, port, debug=True)