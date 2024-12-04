import xmlrpc.client

# Nos conectamos al servidor en localhost y el puerto 8000
servidor = xmlrpc.client.ServerProxy("http://localhost:8000/")

# Llamamos a la función remota 'hola_mundo' y mostramos la respuesta
respuesta = servidor.hola_mundo()
print(f"Respuesta del servidor: {respuesta}")
