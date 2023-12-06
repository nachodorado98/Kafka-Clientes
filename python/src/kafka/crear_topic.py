from confluent_kafka.admin import AdminClient, NewTopic

from .config import SERVIDOR

# Funcion para crear un topic con su nombre
def crearTopic(topic:str)->None:

	admin=AdminClient({"bootstrap.servers":SERVIDOR})

	if topic in admin.list_topics().topics:

		print(f"Topic {topic} creado")
		return

	print(f"Creando topic {topic}...")

	objeto_topic=NewTopic(topic=topic, num_partitions=3, replication_factor=1)

	admin.create_topics([objeto_topic])

	crearTopic(topic)