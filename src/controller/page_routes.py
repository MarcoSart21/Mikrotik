from flask import *
from src.model.busquedas_api import *

page = Blueprint('page', __name__)

@page.route('/')
def index():
    
    datos = buscar_ip()
    colas = obtener_colas()
    
    return render_template('index.html', datos=datos, colas=colas)

@page.route('/prueba')
def prueba():
    
    return render_template('prueba.html')
