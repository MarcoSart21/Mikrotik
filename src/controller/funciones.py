from flask import *
from src.model.api import *

funcion = Blueprint('funcion', __name__)

@funcion.route('/agregar_ip', methods = ['POST'])
def agregar_ip():
    
    if request.method == 'POST':
        
        ip = str(request.form['ip'])
        mascara = str(request.form['mascara'])
        interfaz = str(request.form['interfaz'])
    
        agregar_ip2(ip,mascara,interfaz)
        
        return jsonify({"message": "IP agregada correctamente"}), 200
        
    
    return Response(status=200)

@funcion.route('/agregar_usuario', methods=['POST'])
def agregar_usuario():
    if request.method == 'POST':
        nombre = str(request.form['nombre'])
        contrasena = str(request.form['contrasena'])
        permisos = str(request.form['permisos'])
        Comentario = str(request.form['comentario'])
        
        agregar_usuario2(nombre,contrasena,permisos,Comentario)
        
        return jsonify({"message": "Usuario agregado correctamente"}), 200
    
@funcion.route('/limitar_bh', methods=['POST'])
def limitar_bh():
    if request.method == 'POST':
        
        nombre = str(request.form['nombre-bh'])
        ip = str(request.form['ip-ancho'])
        maximo = int(request.form['max'])
        minimo = int(request.form['min'])
        
        limitar_ancho_banda(nombre,ip,maximo,minimo)
        
        return jsonify({"message": "Ancho de Banda Limitado Correctamente"}), 200

@funcion.route('/editar_bh', methods=['POST'])
def editar_bh():
    if request.method == "POST":
        
        nombre = str(request.form['cola'])
        subida = int(request.form['max2'])
        bajada = int(request.form['min2'])
        
        print(nombre,subida,bajada)
        editar_ancho_banda(nombre,subida,bajada)
        
        return jsonify({"message": "Ancho de Banda Editado"}), 200
    
@funcion.route('/eliminar_bh', methods=['POST'])
def eliminar_bh():
    if request.method == "POST":
     
        nombre = str(request.form['cola2'])
        
        borrar_ancho_banda(nombre)
        
        return jsonify({"message": "Ancho de Banda Editado"}), 200
     