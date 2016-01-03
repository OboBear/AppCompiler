# -*- coding: UTF-8 -*-

from sqlalchemy import Column, String,Integer,DateTime,create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from OrmUtil import *
from datetime import *

# 创建对象的基类:
Base = declarative_base()

# 定义User对象:
class UserModel(Base):
    # 表的名字:
    __tablename__ = 'User'

    # 表的结构:
    userId = Column(String, primary_key=True)
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
    userRegisterTime = Column(DateTime)

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
def getUserByAccount(userId):
    session = getSession()
    user = session.query(UserModel).filter(UserModel.userId == userId).first()
    session.close()
    if user == None:
        print("找不到用户")
    return user
# user = getUserByAccount('1')

def getUserByAccessToken(userAccessToken,loginType):
    session = getSession()
    user = None
    if loginType == 'web':
        user = session.query(UserModel).filter(UserModel.userAccessTokenForWeb == userAccessToken).first()
    if loginType == 'android':
        user = session.query(UserModel).filter(UserModel.userAccessTokenForAndroid == userAccessToken).first()
    if loginType == 'ios':
        user = session.query(UserModel).filter(UserModel.userAccessTokenForIOS == userAccessToken).first()
    if user == None:
        print("找不到用户")
    return user


# user = getUserByAccessToken('3333','android')
# items = vars(user).items()
# items.pop(1)
# for name,value in items:
#       print('%s=%s'%(name,value))
# print(user)
# print(user.__dict__)

# 更新user accessToken
def updateUser(userId,loginType,accessToken):

    session = getSession()
    user = session.query(UserModel).filter(UserModel.userId == userId)
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


# 新建用户
def insertUser(userPhoneNum,userPassWord):
    user = getUserByPhone(userPhoneNum)
    if user!=None:
        errorMsg="该账号已经存在"
        return (False,errorMsg)

    session = getSession()
    userModelArray = session.query(UserModel).order_by(UserModel.userId).all()
    lastUser = UserModel(userId=1000001)
    if len(userModelArray) >= 1:
        lastUser = userModelArray[len(userModelArray) - 1]

    nextUserId = long(lastUser.userId) + 1
    currentTime = datetime.now()
    newUserModel = UserModel(userId=nextUserId,
                             userPhoneNum=userPhoneNum,
                             userPassWord=userPassWord,
                             userRegisterTime=currentTime)
    session.add(newUserModel)
    session.commit()
    session.close()
    return (True,"账号插入成功")

# insertUser(userEmail="7781723@hwe.com",userPassWord="12341234")


