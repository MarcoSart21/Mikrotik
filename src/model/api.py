from librouteros import *
import ipaddress

router_ip = '[fe80::a00:27ff:fe50:e17c%11]'
username = 'admin'
password = 'skul'

def buscar_ip():
    # Conectar al dispositivo MikroTik
    api= connect(username=username, password=password, host=router_ip)

    # Obtener todas las direcciones IP configuradas
    print("Listando todas las IPs agregadas en el dispositivo:")
    ip_addresses = api.path('/ip/address').__call__('print')  # Llama al comando para listar IPs
    
    ips = []
    for ip in ip_addresses:
        ip_network = ipaddress.ip_network(ip['address'], strict=False)  # strict=False permite usar IPs sin máscara
        ips.append(ip_network)  #Agregar solo la dirección de la red
    
    api.close()
    
    return ips

def obtener_colas():
    api= connect(username=username, password=password, host=router_ip)
    
    # Listar todas las colas (simples y otras configuraciones)
    queues = api('/queue/simple/print')  # Este comando obtiene todas las colas

    colas = []
    # Imprimir los límites de ancho de banda de todas las colas
    if queues:
        print("Límites de ancho de banda de las colas configuradas:")
        for queue in queues:
            colas.append({
                    'nombre' : queue['name'], 
                    'ip' : queue['target']
                })
    else:
        print("No se encontraron colas.")
    
    api.close()
    
    return colas    
    

def agregar_ip2(ip,mascara,interfaz):
    api = connect(username=username, password=password, host=router_ip)
    
    ip_address = api.path("ip", "address")
    ip_address.add(address=f"{ip}/{mascara}", interface=interfaz)
    
    api.close()

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
