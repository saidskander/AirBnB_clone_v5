#!/usr/bin/python3
"""from app views getting storage"""
from flask import jsonify
from models import storage
from api.v1.views import app_views


@app_views.route("/status", strict_slashes=False)
def status():
    """status"""
    return jsonify({'status': 'OK'})


@app_views.route("/states", strict_slashes=False)
def stats():
    """Returns states"""
    return jsonify({"amenities": storage.count("Amenity"),
                    "places": storage.count("Place"),
                    "reviews": storage.count("Review"),
                    "states": storage.count("State"),
                    "users": storage.count("User")})
