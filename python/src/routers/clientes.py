from fastapi import APIRouter, status, HTTPException, Depends
from typing import Dict, List
from confluent_kafka import Producer, KafkaException, Consumer
import json
import threading

from src.modelos.cliente import ClienteBBDD
from src.kafka.crear_topic import crearTopic
from src.kafka.config import TOPIC, SERVIDOR
from src.database.conexion import Conexion
from src.database.sesion import crearSesion

router_clientes=APIRouter(prefix="/clientes", tags=["Clientes"])

crearTopic(TOPIC)

producer=Producer({"bootstrap.servers":SERVIDOR})

@router_clientes.post("", status_code=status.HTTP_201_CREATED, summary="Crea un cliente")
async def crearCliente(cliente:ClienteBBDD)->Dict:

	"""
	Crea un cliente y lo envia a Apache Kafka para su procesamiento.

	Devuelve un mensaje de creacion del cliente.

	## Respuesta

	201 (CREATED): Si se crea el cliente correctamente

	- **Mensaje**: El mensaje de creacion correcto del cliente (str).

	400 (BAD REQUEST): Si no se crea el cliente correctamente

	- **Mensaje**: El mensaje de la excepcion (str).
	"""

	try:

		producer.produce(TOPIC, json.dumps(dict(cliente)))

		producer.flush()
		
		return {"mensaje":"Cliente creado correctamente"}

	except KafkaException as e:

		raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Error en la creacion del cliente")


@router_clientes.get("", status_code=status.HTTP_200_OK, summary="Devuelve los clientes existentes")
async def obtenerClientes(con:Conexion=Depends(crearSesion))->List[Dict]:

	"""
	Devuelve los diccionarios asociados a los clientes disponibles en la BBDD.

	## Respuesta

	200 (OK): Si se obtienen los clientes correctamente

	- **Usuario**: El usuario del cliente (str).

	404 (NOT FOUND): Si no se obtienen los clientes correctamente

	- **Mensaje**: El mensaje de la excepcion (str).
	"""

	clientes=con.obtenerClientes()

	con.cerrarConexion()

	if clientes is None:

		raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Clientes no existentes")

	return clientes


# Funcion para consumir los mensajes de Kafka
def consumirMensajes()->None:
	
	consumer=Consumer({"bootstrap.servers": SERVIDOR, "group.id":"grupo1"})

	consumer.subscribe([TOPIC])

	print("Escuchando...")

	while True:

		mensaje=consumer.poll(timeout=100)

		if mensaje is None:

			continue

		if mensaje.error():

			if mensaje.error().code()==KafkaError._PARTITION_EOF:

				continue

			else:

				print(mensaje.error())

				break

		mensaje_recibido=json.loads(mensaje.value().decode("utf-8"))

		con=Conexion()

		con.insertarCliente(mensaje_recibido["usuario"],
							mensaje_recibido["nombre"],
							mensaje_recibido["apellido1"],
							mensaje_recibido["apellido2"],
							mensaje_recibido["edad"])

		con.cerrarConexion()


threading.Thread(target=consumirMensajes, daemon=True).start()