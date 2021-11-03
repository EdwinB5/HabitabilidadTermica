from flask import Flask, jsonify
app = Flask(__name__)

@app.route('/')
def home():
	'''
	Vista básica del proyecto

	:returns: regresa un json básico
	:rtype: json
	'''
	home = {'titulo':'home', 'numero': 2, 'activo': True}

	return jsonify(home)

def run(host, port):
	'''
	Esta función pone a correr la aplicación flask

	:param host: esta es la dirección en la que se aloja la aplicación
	:type host: str
	:param port: el puerto donde se aloja la aplicación
	:type port: int
	'''
	app.run(host, port, debug=True)