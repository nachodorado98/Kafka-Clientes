import time

def test_pagina_agregar_cliente(cliente, conexion):

	respuesta=cliente.post("/clientes", json={"usuario":"nacho98","nombre":"Nacho","apellido1":"Dorado","apellido2":"Ruiz", "edad":25})

	contenido=respuesta.json()

	assert respuesta.status_code==201
	assert "mensaje" in contenido

	time.sleep(2)

	conexion.c.execute("SELECT * FROM clientes")

	clientes=conexion.c.fetchall()

	assert len(clientes)==1

def test_pagina_agregar_varios_clientes(cliente, conexion):

	cliente.post("/clientes", json={"usuario":"nacho98","nombre":"Nacho","apellido1":"Dorado","apellido2":"Ruiz", "edad":25})
	cliente.post("/clientes", json={"usuario":"nacho98","nombre":"Nacho","apellido1":"Dorado","apellido2":"Ruiz", "edad":25})
	cliente.post("/clientes", json={"usuario":"nacho98","nombre":"Nacho","apellido1":"Dorado","apellido2":"Ruiz", "edad":25})
	cliente.post("/clientes", json={"usuario":"nacho98","nombre":"Nacho","apellido1":"Dorado","apellido2":"Ruiz", "edad":25})
	cliente.post("/clientes", json={"usuario":"nacho98","nombre":"Nacho","apellido1":"Dorado","apellido2":"Ruiz", "edad":25})
	cliente.post("/clientes", json={"usuario":"nacho98","nombre":"Nacho","apellido1":"Dorado","apellido2":"Ruiz", "edad":25})

	time.sleep(2)

	conexion.c.execute("SELECT * FROM clientes")

	clientes=conexion.c.fetchall()

	assert len(clientes)==6