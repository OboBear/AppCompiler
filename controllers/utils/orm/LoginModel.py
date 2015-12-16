# -*- coding: UTF-8 -*-

from sqlalchemy import Column, String,Integer,create_engine,DateTime
from sqlalchemy import func
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from  OrmUtil import *
from datetime import *

# 创建对象的基类:
Base = declarative_base()

class LoginModel(Base):
    # 表的名字:
    __tablename__ = 'Login'
    # 表的结构:
    loginId = Column(String, primary_key=True)
    userAccount = Column(String)
    loginTime = Column(DateTime)
    loginPosition = Column(String)
    loginType = Column(String)
    loginAccessToken = Column(String)


from random import Random
def random_str(randomlength=8):
    str = ''
    chars = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789'
    length = len(chars) - 1
    random = Random()
    for i in range(randomlength):
        str+=chars[random.randint(0, length)]
    return str

def Test():
        # loginModel = LoginModel(loginId='1',userAccount='1',loginPosition='123',loginType='web',loginAccessToken='fasd')
        session = getSession()

        loginModelArray = session.query(LoginModel).order_by(LoginModel.loginId).all()

        lastLogin = loginModelArray[len(loginModelArray)-1]
        nextLoginId = long(lastLogin.loginId) + 1
        nextLoginId = str(nextLoginId)
        currentTime = datetime.now()

        print(nextLoginId)

        print(lastLogin.loginPosition)

        #
        # print 'now():', datetime.now()

        loginAccessToken = random_str(16)
        loginModel = LoginModel(loginId=nextLoginId,userAccount='1',loginTime=currentTime,loginPosition='123',loginType='web',loginAccessToken=loginAccessToken)
        #
        # # 添加到session:
        session.add(loginModel)
        # # 提交即保存到数据库:
        session.commit()
        # # 关闭session:
        session.close()
        return 'success'

Test()