from flask import Flask

# 1. Creamos la aplicación directamente sin configuraciones externas
app = Flask(__name__)

# 2. Importamos las rutas al final para evitar el bucle circular
from app import routes