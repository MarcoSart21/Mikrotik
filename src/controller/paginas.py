from flask import *
from src.model.api import *

routes = Blueprint('routes', __name__)

@routes.route('/')
def index():
    
    datos = buscar_ip()
    colas = obtener_colas()
    
    return render_template('index.html', datos=datos, colas=colas)

@routes.route('/prueba')
def prueba():
    
    return render_template('prueba.html')
