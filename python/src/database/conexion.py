import psycopg2
from psycopg2.extras import RealDictCursor
from typing import List, Dict, Optional

from .confconexion import *

# Clase para la conexion a la BBDD
class Conexion:

	def __init__(self)->None:

		try:
			
			self.bbdd=psycopg2.connect(host=HOST, user=USUARIO, password=CONTRASENA, port=PUERTO, database=BBDD)
			self.c=self.bbdd.cursor(cursor_factory=RealDictCursor)

		except psycopg2.OperationalError as e:

			print("Error en la conexion a la BBDD")

	# Metodo para cerrar la conexion a la BBDD
	def cerrarConexion(self)->None:

		self.c.close()
		self.bbdd.close()

	# Metodo para confirmar una accion
	def confirmar(self)->None:

		self.bbdd.commit()

	# Metodo para insertar un cliente
	def insertarCliente(self, usuario:str, nombre:str, apellido1:str, apellido2:str, edad:int)->None:

		self.c.execute("""INSERT INTO clientes (usuario, nombre, apellido1, apellido2, edad)
						VALUES (%s, %s, %s, %s, %s)""",
						(usuario, nombre, apellido1, apellido2, edad))

		self.confirmar()

	# Metodo para obtener los clientes
	def obtenerClientes(self)->Optional[List[Dict]]:

		self.c.execute("""SELECT usuario
							FROM clientes""")

		clientes=self.c.fetchall()

		return None if clientes==[] else clientes