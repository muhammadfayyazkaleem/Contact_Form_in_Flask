from flask import Flask
from flask_sqlalchemy import SQLAlchemy 
from os import path

db = SQLAlchemy()
db_name = "contact_info.db"

def create_app():

    app = Flask(__name__)
    app.config['SECRET_KEY'] = "Fayyaz.Kaleem724"
    app.config["SQLALCHEMY_DATABASE_URI"] = f'sqlite:///{db_name}'
    
    db.init_app(app)

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix ='/')
    app.register_blueprint(auth , url_prefix = '/')

    from .models import ContactInfo

    create_database(app)

    return app

def create_database(app):
    if not path.exists('website/' + db_name):
        with app.app_context():
            db.create_all()
            print('Database Created!')