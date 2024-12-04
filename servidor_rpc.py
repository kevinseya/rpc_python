from xmlrpc.server import SimpleXMLRPCServer

# Definimos la función que el cliente podrá llamar
def hola_mundo():
    return "¡Hola, mundo desde el servidor RPC!"

# Creamos el servidor en localhost y el puerto 8000
servidor = SimpleXMLRPCServer(("localhost", 8000))
print("Servidor RPC escuchando en el puerto 8000...")

# Registramos la función para que esté disponible para el cliente
servidor.register_function(hola_mundo, "hola_mundo")

# Iniciamos el servidor (queda en espera de llamadas del cliente)
servidor.serve_forever()
