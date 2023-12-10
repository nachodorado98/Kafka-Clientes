def test_insertar_cliente(conexion):

	conexion.insertarCliente("nacho98", "Nacho", "Dorado", "Ruiz", 25)

	conexion.c.execute("SELECT * FROM clientes")

	clientes=conexion.c.fetchall()

	assert len(clientes)==1

def test_insertar_varios_clientes(conexion):

	for _ in range(5):

		conexion.insertarCliente("nacho98", "Nacho", "Dorado", "Ruiz", 25)

	conexion.c.execute("SELECT * FROM clientes")

	clientes=conexion.c.fetchall()

	assert len(clientes)==5

def test_obtener_clientes_no_existen(conexion):

	assert conexion.obtenerClientes() is None

def test_obtener_clientes_existen(conexion):

	conexion.insertarCliente("nacho98", "Nacho", "Dorado", "Ruiz", 25)
	conexion.insertarCliente("nacho98", "Nacho", "Dorado", "Ruiz", 25)
	conexion.insertarCliente("nacho98", "Nacho", "Dorado", "Ruiz", 25)
	conexion.insertarCliente("nacho98", "Nacho", "Dorado", "Ruiz", 25)

	clientes=conexion.obtenerClientes()

	assert len(clientes)==4

	for cliente in clientes:

		assert "usuario" in cliente