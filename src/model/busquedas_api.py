from src.model.conexion_api import *
import ipaddress

#solo busca las direcciones network
def buscar_network():
    # Conectar al dispositivo MikroTik
    api= connect(username=username, password=password, host=router_ip)

    # Obtener todas las direcciones IP configuradas
    print("Listando todas las IPs agregadas en el dispositivo:")
    ip_addresses = api.path('/ip/address').__call__('print')  # Llama al comando para listar IPs
    
    networks = []
    for ip in ip_addresses:
        ip_network = ipaddress.ip_network(ip['address'], strict=False)  # strict=False permite usar IPs sin máscara
        networks.append(ip_network)  #Agregar solo la dirección de la red
    
    api.close()
    
    return networks

def buscar_ip():
    # Conectar al dispositivo MikroTik
    api= connect(username=username, password=password, host=router_ip)

    # Obtener todas las direcciones IP configuradas
    print("Listando todas las IPs agregadas en el dispositivo:")
    ip_addresses = api.path('/ip/address').__call__('print')  # Llama al comando para listar IPs
    
    ips = []
    for ip in ip_addresses:
        ips.append(ip['address'])  #Agregar solo la dirección de la red
    
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
