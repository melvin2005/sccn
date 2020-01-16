from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column
from sqlalchemy import Integer,DateTime,String
from sqlalchemy import create_engine
from sccn import dbconn

class LoginUser(dbconn.Model):
    __tablename__ = 'ADMIN_USER'

    id = Column(Integer, primary_key=True)
    name = Column(String(50),index=True,nullable=False)
    login_pwd = Column(String(100))