# -*- coding: UTF-8 -*-

from sqlalchemy import Column, String,Integer,create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from OrmUtil import *

# 创建对象的基类:
Base = declarative_base()

# 定义User对象:
class UserModel(Base):
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

# 通过Email获取User
def getUserByEmail(userEmail):
    session = getSession()
    user = session.query(UserModel).filter(UserModel.userEmail == userEmail).first()
    session.close()
    return user
# getUserByEmailAndPassword('634468123460@qq.com')
# 通过phoneNumber获取User
def getUserByPhone(userPhoneNum):
    session = getSession()
    user = session.query(UserModel).filter(UserModel.userPhoneNum == userPhoneNum).first()
    session.close()
    return user
# getUserByEmailAndPassword('157571156721')

# 通过账号查找User
def getUserByAccount(userAccount):
    session = getSession()
    user = session.query(UserModel).filter(UserModel.userAccount == userAccount).first()
    session.close()
    if user == None:
        print("找不到用户")
    return user
# user = getUserByAccount('1')


# 更新user accessToken
def updateUser(userAccount,loginType,accessToken):

    session = getSession()
    user = session.query(UserModel).filter(UserModel.userAccount == userAccount)
    if len(user.all()) == 0:
        print('不存在该账号')
        return False

    if loginType == 'web':
        user.update({UserModel.userAccessTokenForWeb: accessToken})
    if loginType == 'android':
        user.update({UserModel.userAccessTokenForAndroid: accessToken})
    if loginType == 'ios':
        user.update({UserModel.userAccessTokenForIOS: accessToken})
    session.commit()
    session.close()
    return True

