from flask import Flask, jsonify
from werkzeug.middleware.dispatcher import DispatcherMiddleware
from werkzeug.wrappers import Response

# carrega as variáveis do .env (senha, banco etc.)
# load_dotenv()

app = Flask(__name__)  

app.secret_key = "ksksks"



from app.routes import * #esse seria o caminho para poder chegar até os ingredientes
# from .models import models




