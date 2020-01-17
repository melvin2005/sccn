from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column,Integer,DateTime,String,create_engine
from sccn import dbconn

class LoginUser(dbconn.Model):
    __tablename__ = 'ADMIN_USER'

    id = Column(Integer, primary_key=True)
    login_name = Column(String(50),index=True,nullable=False)
    login_pwd = Column(String(100))