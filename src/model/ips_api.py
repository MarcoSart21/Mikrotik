from src.model.conexion_api import *

def agregar_ip2(ip,mascara,interfaz):
    api = connect(username=username, password=password, host=router_ip)
    
    ip_address = api.path("ip", "address")
    ip_address.add(address=f"{ip}/{mascara}", interface=interfaz)
    
    api.close()