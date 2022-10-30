from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
# import os
db = SQLAlchemy()

def create_app():
    # file_path = os.path.abspath(os.getcwd()) + "C:/Users/amuls/PycharmProjects/To-Do App/instance/database.db"
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'Always Be Honest'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///../instance/database.db'
    db.init_app(app)

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    from .models import User, Note

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    return app






