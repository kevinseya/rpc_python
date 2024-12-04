# Proyecto de RPC con Python

Este proyecto implementa un **sistema de comunicación RPC (Remote Procedure Call)** utilizando Python. Consiste en un servidor y un cliente que se comunican entre sí para ejecutar funciones de manera remota.

## Archivos del Proyecto

- `servidor_rpc.py`: Script que implementa el servidor RPC.
- `cliente_rpc.py`: Script que implementa el cliente RPC.

## Requisitos

Para ejecutar el proyecto, necesitas instalar Python 3.x y las siguientes dependencias:

```bash
pip install xmlrpc-server
```
## Ejecución
1. Ejecutar el Servidor

Primero, inicia el servidor RPC:
```bash
python servidor_rpc.py
```
2. Ejecutar el Cliente

Luego, en una terminal separada, ejecuta el cliente:
```bash
python client_rpc.py 
```
## Funcionalidades
- Servidor RPC: El servidor escucha solicitudes de clientes y ejecuta funciones remotas.
- Cliente RPC: El cliente envía solicitudes al servidor y recibe respuestas con los resultados de las funciones ejecutadas.
