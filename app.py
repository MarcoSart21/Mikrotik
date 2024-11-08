from flask import *
from src.model.api import *
from src.controller.paginas import *
from src.controller.funciones import *


app = Flask(__name__, 
            template_folder='src/view/templates',
            static_folder='src/view/static')

app.register_blueprint(routes)

app.register_blueprint(funcion)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port = 5000, debug=True)