from flask import Flask
from flask_sqlalchemy import SQLAlchemy 
from os import path
from flask_login import LoginManager
from flask_mail import Mail



db = SQLAlchemy()
mail = Mail()
db_name = "contact_info.db"


def create_app():

    app = Flask(__name__)
    app.config['SECRET_KEY'] = "Fayyaz.Kaleem724"
    app.config["SQLALCHEMY_DATABASE_URI"] = f'sqlite:///{db_name}'
    app.config['MAIL_SERVER']='smtp.gmail.com'
    app.config['MAIL_PORT'] = 465
    app.config['MAIL_USERNAME'] = 'fayyazkaleem39@gmail.com'
    app.config['MAIL_PASSWORD'] = 'Fayyaz.Kaleem.724'
    app.config['MAIL_USE_TLS'] = False
    app.config['MAIL_USE_SSL'] = True
    

    mail.init_app(app)
    db.init_app(app)
 
    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix ='/')
    app.register_blueprint(auth , url_prefix = '/')

    from .models import ContactInfo , User

    create_database(app)

    login_manager = LoginManager()
    login_manager.login_view = 'auth.admin_login'
    login_manager.init_app(app)


    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))


    return app

def create_database(app):
    if not path.exists('website/' + db_name):
        with app.app_context():
            db.create_all()
            print('Database Created!')