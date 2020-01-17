class BaseConfig(object):
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:qazwsx@10.11.100.130:3306/hlwxz01?charset=utf8"
    SECRET_KEY = "ghca@222"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class DevConfigAtHome(BaseConfig):
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:qazwsx@192.168.1.13:3306/hlwxz01?charset=utf8"
    SECRET_KEY = "ghca@222"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class DevConfig(BaseConfig):
    """
    开发环境配置
    """
    pass


class ProductConfig(BaseConfig):
    """
    生产环境配置
    """
    pass