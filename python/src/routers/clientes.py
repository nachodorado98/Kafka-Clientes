from fastapi import APIRouter, status, HTTPException
from typing import Dict
from confluent_kafka import Producer, KafkaException
import json

from src.modelos.cliente import ClienteBBDD
from src.kafka.crear_topic import crearTopic
from src.kafka.config import TOPIC, SERVIDOR

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