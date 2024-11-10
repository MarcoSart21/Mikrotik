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