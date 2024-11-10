from src.model.conexion_api import *


def limitar_ancho_banda(nombre, ip, maximo, minimo):
    api = connect(username=username, password=password, host=router_ip)

    queue_simple = api.path("queue", "simple")
    queue_simple.add(
        name = nombre,
        target = ip,
        **{
            'max-limit': f"{maximo}M/{minimo}M"
        }
    )

    print(f"Limitación de ancho de banda aplicada a la IP {ip}")

    api.close()
    

def editar_ancho_banda(nombre,subida,bajada):
    api= connect(username=username, password=password, host=router_ip)

    # Definir el nombre de la cola que quieres editar
    queue_name_to_edit = nombre  # Cambia esto al nombre exacto de la cola

    # Listar todas las colas para encontrar el ID de la cola
    queues = api('/queue/simple/print')

    # Buscar la cola con el nombre especificado
    queue = next((q for q in queues if q['name'] == queue_name_to_edit), None)

    if queue:
        queue_id = queue['.id']
        print(f"Cola encontrada. ID: {queue_id}")

        # Modificar los límites de la cola (por ejemplo, 2 Mbps de subida y bajada)
        updated_queue_data = {
            'max-limit': f'{subida}M/{bajada}M'  # Cambia esto al nuevo límite que desees
        }

        # Intentar editar la cola
        try:
            response = api('/queue/simple/set', **updated_queue_data, **{'.id': queue_id})
            print("Límite de ancho de banda actualizado correctamente.")
            print(f"Respuesta de la modificación: {list(response)}")  # Convierte el generador a lista para ver el resultado
        except Exception as e:
            print(f"Error al actualizar la cola: {e}")
    else:
        print(f"No se encontró la cola con nombre: {queue_name_to_edit}")

    # Verificar si el cambio fue exitoso mostrando la configuración actual de la cola
    try:
        # Usar el ID de la cola para obtener la configuración de la cola modificada
        updated_queue = api('/queue/simple/print', **{'=.id': queue_id})  # Modificar la forma en que pasas los parámetros
        print("Configuración actual de la cola después de la modificación:")
        print(updated_queue)
    except Exception as e:
        # print(f"Error al obtener la configuración de la cola después de la modificación: {e}")
        print(f"Error al obtener la configuración de la cola después de la modificación:")
        

    api.close()
    
    
def borrar_ancho_banda(nombre):
    api= connect(username=username, password=password, host=router_ip)
    
    # Encuentra la cola por nombre o identificador
    queue_name = nombre  # Cambia esto por el nombre de tu cola
    query = api.path('queue/simple')

    # Busca la cola que deseas eliminar
    for item in query:
        if item['name'] == queue_name:
            # Elimina la cola usando el identificador
            api.path('queue/simple').remove(item['.id'])
            print(f'La cola "{queue_name}" ha sido eliminada.')
            break
    else:
        print(f'No se encontró una cola con el nombre "{queue_name}".')
    
    api.close()
