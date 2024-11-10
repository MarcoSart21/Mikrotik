from src.model.conexion_api import *


def agregar_usuario2(nombre,contrasena,permisos,Comentario):
    api = connect(username=username, password=password, host=router_ip)
    
    # Configuración del nuevo usuario
    nuevo_usuario = {
        'name': nombre,
        'password': contrasena,
        'group': permisos,
        'comment': Comentario
    }
    
    # Intentar crear el usuario
    response = api.path('/user').__call__('add', **nuevo_usuario)
    print(f"Usuario '{nuevo_usuario['name']}' creado exitosamente. Respuesta: {list(response)}")
    
    api.close()