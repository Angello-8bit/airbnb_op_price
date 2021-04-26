  
from flask_sqlalchemy import SQLAlchemy

DB = SQLAlchemy()

class price(DB.Model):
    id = DB.Column(DB.Integer, primary_key=True)
    price_id = DB.Column(DB.String(50), nullable=False)
    price = DB.Column(DB.String(50), nullable=False)
    city = DB.Column(DB.String(50), nullable=False)
    min_nights = DB.Column(DB.String(50), nullable=False)

