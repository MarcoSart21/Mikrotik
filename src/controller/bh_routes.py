from flask import *
from src.model.bh_api import *

#bh significa banda hancha
bh = Blueprint('bh', __name__)

@bh.route('/limitar_bh', methods=['POST'])
def limitar_bh():
    if request.method == 'POST':
        
        nombre = str(request.form['nombre-bh'])
        ip = str(request.form['ip-ancho'])
        maximo = int(request.form['max'])
        minimo = int(request.form['min'])
        
        limitar_ancho_banda(nombre,ip,maximo,minimo)
        
        return jsonify({"message": "Ancho de Banda Limitado Correctamente"}), 200

@bh.route('/editar_bh', methods=['POST'])
def editar_bh():
    if request.method == "POST":
        
        nombre = str(request.form['cola'])
        subida = int(request.form['max2'])
        bajada = int(request.form['min2'])
        
        print(nombre,subida,bajada)
        editar_ancho_banda(nombre,subida,bajada)
        
        return jsonify({"message": "Ancho de Banda Editado"}), 200
    
@bh.route('/eliminar_bh', methods=['POST'])
def eliminar_bh():
    if request.method == "POST":
     
        nombre = str(request.form['cola2'])
        
        borrar_ancho_banda(nombre)
        
        return jsonify({"message": "Ancho de Banda Editado"}), 200