def test_pagina_agregar_cliente(cliente):

	respuesta=cliente.post("/clientes", json={"usuario":"nacho98","nombre":"Nacho","apellido1":"Dorado","apellido2":"Ruiz", "edad":25})

	contenido=respuesta.json()

	assert respuesta.status_code==201
	assert "mensaje" in contenido