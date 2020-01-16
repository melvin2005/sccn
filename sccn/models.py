from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column
from sqlalchemy import Integer,DateTime,String
from sqlalchemy import create_engine
from sccn import dbconn

class LoginUser(dbconn.Model):
    pass