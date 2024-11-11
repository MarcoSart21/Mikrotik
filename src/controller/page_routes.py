from flask import *
from src.model.busquedas_api import *

page = Blueprint('page', __name__)

@page.route('/')
def index():
    
    networks = buscar_network()
    colas = obtener_colas()
    ips = buscar_ip()
    
    return render_template('index.html', ips=ips, networks=networks, colas=colas)

@page.route('/prueba')
def prueba():
    
    return render_template('prueba.html')
