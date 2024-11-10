from flask import *
from src.model.usuarios_api import *

user = Blueprint('user', __name__)

@user.route('/agregar_usuario', methods=['POST'])
def agregar_usuario():
    if request.method == 'POST':
        nombre = str(request.form['nombre'])
        contrasena = str(request.form['contrasena'])
        permisos = str(request.form['permisos'])
        Comentario = str(request.form['comentario'])
        
        agregar_usuario2(nombre,contrasena,permisos,Comentario)
        
        return jsonify({"message": "Usuario agregado correctamente"}), 200
    
