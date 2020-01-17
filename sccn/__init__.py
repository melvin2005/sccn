from flask import Flask,session,request,redirect
from flask_session import Session

from flask_sqlalchemy import SQLAlchemy
dbconn = SQLAlchemy()

#注意这里导入不能提到上层
from .views.login import lg
from .views.index import idx

def create_app():
    app = Flask(__name__)

    #读取配置文件
    app.config.from_object('settings.BaseConfig')

    #注册蓝图
    app.register_blueprint(lg)
    app.register_blueprint(idx)

    dbconn.init_app(app)

    return app