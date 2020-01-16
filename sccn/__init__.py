from flask import Flask
from flask_session import Session

from flask_sqlalchemy import SQLAlchemy
dbconn = SQLAlchemy()

from .views.login import lg

def create_app():
    app = Flask(__name__)

    #读取配置文件
    app.config.from_object('settins.BaseConfig')

    #注册蓝图
    app.register_blueprint(lg)

    return app