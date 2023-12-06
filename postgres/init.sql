CREATE DATABASE bbdd_clientes;

\c bbdd_clientes;

CREATE TABLE clientes (id SERIAL PRIMARY KEY,
						usuario VARCHAR(20),
						nombre VARCHAR(20),
						apellido1 VARCHAR(20),
						apellido2 VARCHAR(20),
						edad INT);