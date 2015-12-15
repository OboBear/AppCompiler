# -*- coding: UTF-8 -*-

from sqlalchemy import Column, String,Integer,create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


# 创建对象的基类:
Base = declarative_base()

# 定义User对象:
class User(Base):
    # 表的名字:
    __tablename__ = 'User'

    # 表的结构:
    userAccount = Column(String, primary_key=True)

    userEmail = Column(String)
    userPassWord = Column(String)
    userPhoneNum = Column(String)

    userNickName = Column(String)
    userGender = Column(String)
    userAge = Column(Integer)
    userCity = Column(String)
    userAccessTokenForWeb = Column(String)
    userAccessTokenForAndroid = Column(String)
    userAccessTokenForIOS = Column(String)

