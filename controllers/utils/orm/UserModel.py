# -*- coding: UTF-8 -*-

from sqlalchemy import Column, String,Integer,create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from OrmUtil import *
import json

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

# 通过账号密码获取User
def getUserByEmailAndPassword(userEmail,userPassword):
    session = getSession()
    user = session.query(UserModel).filter(UserModel.userEmail == userEmail).first()
    session.close()
    if user == None:
        print("找不到用户")
        return (None,'找不到用户')
    if user.userPassWord != userPassword:
        print("密码不正确")
        return (None,'密码不正确')
    return (user,'成功搜索')
# getUserByEmailAndPassword('634468460@qq.com','12341234')


# 通过账号查找User
def getUserByAccount(userAccount):
    session = getSession()
    user = session.query(UserModel).filter(UserModel.userAccount == userAccount).first()
    session.close()
    if user == None:
        print("找不到用户")
    return user

user = getUserByAccount('1')
# print(json.dumps( user.__dict__ ))
print( user.userAccessTokenForWeb )
for property, value in vars(user).iteritems():
    print property, ": ", value

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

