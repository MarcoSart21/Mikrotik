from flask import *
from src.model.ips_api import *

ips = Blueprint('ips', __name__)

@ips.route('/agregar_ip', methods = ['POST'])
def agregar_ip():
    
    if request.method == 'POST':
        
        ip = str(request.form['ip'])
        mascara = str(request.form['mascara'])
        interfaz = str(request.form['interfaz'])
    
        agregar_ip2(ip,mascara,interfaz)
        
        return jsonify({"message": "IP agregada correctamente"}), 200
        
    
    return Response(status=200)

@ips.route('/editar_ip', methods = ['POST'])
def editar_ip():
    
    if request.method == 'POST':
        
        antigua_ip = str(request.form['ip-antigua'])
        ip = str(request.form['ip-nueva'])
        mascara = str(request.form['mascara-nueva'])
        interfaz = str(request.form['interfaz-nueva'])
        
        editar_ip2(antigua_ip,ip,mascara,interfaz)
        
        return jsonify({"message": "IP editada correctamente"}), 200
    
@ips.route('/eliminar_ip', methods=['POST'])
def eliminar_ip():
    
    if request.method == 'POST':
        
        ip = str(request.form['ip-eliminar'])
        
        eliminar_ip2(ip)
        
        return jsonify({"message": "IP eliminada correctamente"}), 200
        