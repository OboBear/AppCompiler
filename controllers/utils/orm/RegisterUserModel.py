# -*- coding: UTF-8 -*-
from sqlalchemy import Column, String, Integer, create_engine, DateTime
from sqlalchemy import func
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from OrmUtil import *
from datetime import *

from ..util import *

# 创建对象的基类:
Base = declarative_base()

class RegisterUserModel(Base):
    # 表的名字:
    __tablename__ = 'RegisterUser'

    userPhoneNum = Column(String, primary_key=True)
    userIdentifyCode = Column(String)
    registerTime = Column(DateTime)

def insertRegister(userPhoneNum):
    registerUserModel = findRegister(userPhoneNum)
    if registerUserModel != None:
        return registerUserModel.userIdentifyCode
    session = getSession()
    registerTime = datetime.now()
    userIdentifyCode = random_num(4)
    registerUserModel = RegisterUserModel(userPhoneNum=userPhoneNum,userIdentifyCode=userIdentifyCode,registerTime=registerTime)
    # 添加到session:
    session.add(registerUserModel)
    # 提交即保存到数据库:
    session.commit()
    # 关闭session:
    session.close()
    return userIdentifyCode

def findRegister(userPhoneNum):
    session = getSession()
    return session.query(RegisterUserModel).filter(RegisterUserModel.userPhoneNum == userPhoneNum).first()

# 获取指定号码的验证码
def getRegisterIdentifyCode(userPhoneNum):
    registerUserModel = findRegister(userPhoneNum)
    if registerUserModel==None:
        return None
    return registerUserModel.userIdentifyCode
# print(getRegisterIdentifyCode(15757115391))