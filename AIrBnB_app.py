from flask import Flask, render_template, request
from .models import DB

def create_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///db.sqlite3'
    app.config["SQLALCHEMY_MODIFICATIONS"] = False
    DB.init_app(app)
    

    @app.route("/")
    def root():
        DB.drop_all()
        DB.create_all()
        .query.all()
        return render_template("base.html")
    
    @app.route('/reset')
    def reset():
        DB.drop_all()
        DB.create_all()
        return render_template("base.html", title="RESET", .query.all())
