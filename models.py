"""SQLAlchemy models for Airbnb"""
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import pickle
import requests
import json
from flask_sqlalchemy import SQLAlchemy

DB = SQLAlchemy()

dataset = pd.read_csv('airbnb_data.csv.csv')
X = dataset.drop(columns=['price'])
y = dataset["price"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.33, random_state = 0)

regressor = LinearRegression()
regressor.fit(X_train, y_train)
y_pred = regressor.predict(X_test)

model = pickle.load(open('model.pkl','rb'))
print(model.predict([[1.8]]))

pickle.dump(regressor, open('model.pkl','wb'))

class Listing(DB.Model):
    """Airbnb listings corresponding to Hosts"""
    id = DB.Column(DB.Integer, primary_key=True)
    property_type = DB.Column(DB.String, nullable=False)
    room_type = DB.Column(DB.String, nullable=False)
    accommodates = DB.Column(DB.Integer, nullable=False)
    bedrooms = DB.Column(DB.Integer, nullable=False)
    baths = DB.Column(DB.Numeric, nullable=False)
    zip = DB.Column(DB.Integer, nullable=False)

    def __repr__(self):
        rep = f"""Id: {self.id} Property Type: {self.property_type} Room Type: {self.room_type} Accommodates: {self.accommodates} Bedrooms: {self.bedrooms} Baths: {self.baths} Zip: {self.zip}"""
        return rep
