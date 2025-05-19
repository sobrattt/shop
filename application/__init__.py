from flask import Flask
from application.routes import auth, main, shop
from . import config


app = Flask(__name__, template_folder=config.TEMPLATES_FOLDER)
app.register_blueprint(auth.router)
app.register_blueprint(main.router)
app.register_blueprint(shop.router)

app.secret_key = "qwerty32"