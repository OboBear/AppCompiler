# -*- coding: UTF-8 -*-

from sqlalchemy import Column, String, Integer, create_engine, DateTime
from sqlalchemy import func
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from OrmUtil import *
from datetime import *

# 创建对象的基类:
Base = declarative_base()


class LoginModel(Base):
    # 表的名字:
    __tablename__ = 'Login'
    # 表的结构:
    loginId = Column(String, primary_key=True)
    userId = Column(String)
    loginAccount = Column(String)
    loginTime = Column(DateTime)
    loginPosition = Column(String)
    loginType = Column(String)
    loginAccessToken = Column(String)
    loginIp = Column(String)

def getLastLogin():
    session = getSession()
    loginModelArray = session.query(LoginModel).order_by(LoginModel.loginId).all()
    session.close()
    lastLogin = LoginModel(loginId=1000001)
    if len(loginModelArray) >= 1:
        lastLogin = loginModelArray[len(loginModelArray) - 1]
    return lastLogin

def insertLogin(userId,loginAccount, loginPosition, loginType, loginAccessToken,loginIp):
    session = getSession()
    nextLoginId = long(getLastLogin().loginId) + 1
    nextLoginId = str(nextLoginId)
    currentTime = datetime.now()
    loginModel = LoginModel(loginId=nextLoginId,
                            userId=userId,
                            loginAccount=loginAccount,
                            loginTime=currentTime,
                            loginPosition=loginPosition,
                            loginType=loginType,
                            loginAccessToken=loginAccessToken,
                            loginIp=loginIp)
    # 添加到session:
    session.add(loginModel)
    # 提交即保存到数据库:
    session.commit()
    # 关闭session:
    session.close()
    return 'success'


