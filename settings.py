class BaseConfig(object):
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:qazwsx@10.11.100.130:3306/melvinDB?charset=utf8"
    SECRET_KEY = "ghca@222"

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