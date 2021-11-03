import config.config as config
from core.app import run 

def run_app(host, port):
	'''
	Esta función se encarga de correr el servidor
	llamando, la aplicación flask desde el core

	:param host: esta es la dirección en la que se aloja la aplicación
	:type host: str
	:param port: el puerto donde se aloja la aplicación
	:type port: int
	'''
	run(host, port)

if __name__ == '__main__':
	'''
	Este es el main del proyecto
	'''
	run_app(config.host, config.port)
