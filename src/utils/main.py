# main.py

import os
import logging
from flask import Flask, jsonify
from api_service.config import Config
from api_service.database import db
from api_service.routes import api

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    db.init_app(app)
    app.register_blueprint(api)
    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)