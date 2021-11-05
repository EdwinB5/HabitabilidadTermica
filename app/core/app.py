from flask import Flask, render_template

app = Flask(__name__, template_folder='view', static_folder='view/static/')

@app.route('/')
def datos_entrada():
	'''
	Vista principal del proyecto, formulario de entrada
	'''
	return render_template('index.html')

@app.route('/salida')
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