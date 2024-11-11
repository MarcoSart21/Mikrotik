from src.model.conexion_api import *
from librouteros.exceptions import *

def agregar_ip2(ip,mascara,interfaz):
    api = connect(username=username, password=password, host=router_ip)
    
    ip_address = api.path("ip", "address")
    ip_address.add(address=f"{ip}/{mascara}", interface=interfaz)
    
    api.close()
    
def editar_ip2(antigua_ip,ip,mascara,interfaz):
    api = connect(host=router_ip, username=username, password=password)

    nueva_ip = f"{ip}/{mascara}" 

    # Buscar la entrada con la IP existente
    address_list = api.path("ip", "address")
    existing_ip = None
    for address in address_list:
        if address.get("address") == antigua_ip:
            existing_ip = address
                
            address_list.update(**{".id": existing_ip['.id'], "address": nueva_ip, "interface": interfaz})
            print(f"IP {antigua_ip} actualizada a {nueva_ip}")
        else:
            print("IP no encontrada")
    
    api.close()

def eliminar_ip2(ip):
    print(ip)
    api = connect(host=router_ip, username=username, password=password)

    # Buscar la entrada con la IP existente
    address_list = api.path("ip", "address")
    ip_to_delete = None
    for address in address_list:
        if address.get("address") == ip:
            ip_to_delete = address
            address_list.remove(ip_to_delete['.id'])
            print(f"IP {ip_to_delete['address']} eliminada")
        else:
            print("IP no encontrada")
    
    api.close()
    