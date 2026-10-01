from flask import Flask
from src.main.routes.barcode import barcode_routes_bp

app = Flask(__name__)

app.register_blueprint(barcode_routes_bp)
