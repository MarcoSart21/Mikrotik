from flask import *
# from src.model.api import *
from src.controller.page_routes import *
from src.controller.ip_routes import *
from src.controller.bh_routes import *
from src.controller.user_routes import *



app = Flask(__name__, 
            template_folder='src/view/templates',
            static_folder='src/view/static')

app.register_blueprint(page)

app.register_blueprint(ips)

app.register_blueprint(bh)

app.register_blueprint(user)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port = 5000, debug=True)