from pydantic import BaseModel

class Cliente(BaseModel):

	usuario:str

class ClienteBBDD(Cliente):

	nombre:str
	apellido1:str
	apellido2:str
	edad:int

	class Config:

		json_schema_extra={"example":{"usuario":"nacho98",
										"nombre":"Nacho",
										"apellido1":"Dorado",
										"apellido2":"Ruiz",
										"edad":25}}