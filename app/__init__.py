from flask import Flask
from flask_bootstrap import Bootstrap
from app.views import index, login, main
from app.views.interface import interface_list, variables_list
from app.views.system import sector_list, user_list, items_list, log_list, envi_list

app = Flask(__name__)
app.config.from_object('config')
bootstrap = Bootstrap(app)
app.register_blueprint(index.mod)
app.register_blueprint(login.mod)
app.register_blueprint(main.mod)
app.register_blueprint(user_list.mod)
app.register_blueprint(sector_list.mod)
app.register_blueprint(items_list.mod)
app.register_blueprint(log_list.mod)
app.register_blueprint(envi_list.mod)
app.register_blueprint(interface_list.mod)
app.register_blueprint(variables_list.mod)

from app import views
