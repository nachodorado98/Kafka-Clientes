from src.modelos.cliente import ClienteBBDD

def test_modelo_cliente_bbdd_correcto():

	cliente={"usuario":"nacho98","nombre":"Nacho","apellido1":"Dorado","apellido2":"Ruiz", "edad":25}

	ClienteBBDD(**cliente)