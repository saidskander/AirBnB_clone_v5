#!/usr/bin/env python3
"""Entry point for HolbertonBnB API calls."""

from os import getenv
from flask import Flask, make_response, jsonify
from flask_cors import CORS
from api.v1.views import app_views
from models import storage

# app flask configuration
app = Flask(__name__)
CORS(app, orgins='0.0.0.0')
app.register_blueprint(app_views)


@app.teardown_appcontext
def teardown(self):
    """Closes storage session"""
    storage.close()


if __name__ == "__main__":
    app.run(
        host=getenv("HBNB_API_HOST", default="0.0.0.0"),
        port=getenv("HBNB_API_PORT", default="5000"),
        threaded=True
    )
