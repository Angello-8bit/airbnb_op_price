"""Main file for Airbnb Price Predicter."""

import json
import os
from os import getenv
from tempfile import mkdtemp
import numpy as np
import pandas as pd
from flask import Flask, jsonify, render_template, request
from joblib import load
from .models import DB, Listing


def create_app():

    app = Flask(__name__)

    app.config["SQLALCHEMY_DATABASE_URI"] = getenv(
        "DATABASE_URL")
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    DB.init_app(app)
    features = load_features()


    listing = {}

    @app.route('/')
    def root():
        return render_template('home.html', forms=features, title="Home")

    @app.route('/predict-one')
    def predicting():
        return render_template('elements.html', forms=features, title="predicting")

    @app.route('/reset')
    def test_db():
        listing = {}
        DB.drop_all()
        DB.create_all()
        return "DB created"

    return app


def load_features():
    feature_order = get_feature_orders()
    with open('features.json') as file:
        all_possible = json.load(file)
        features = {feature: all_possible[feature]
                    for feature in feature_order}
        return features


def get_feature_orders():
    feature_order = [
        "property_type",
        "room_type",
        "accommodates",
        "bedrooms",
        "baths",
        "zip",
    ]
    return feature_order



