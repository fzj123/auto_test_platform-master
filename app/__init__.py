from flask import Flask
from flask_bootstrap import Bootstrap
from app.views import index,login,main,user_list

app = Flask(__name__)
app.config.from_object('config')
bootstrap = Bootstrap(app)
app.register_blueprint(index.mod)
app.register_blueprint(login.mod)
app.register_blueprint(main.mod)
app.register_blueprint(user_list.mod)

from app import views
