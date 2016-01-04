# -*- coding: UTF-8 -*-

from sqlalchemy import Column, String,Integer,DateTime,create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from OrmUtil import *
from datetime import *
from json import *
import json

# 创建对象的基类:
Base = declarative_base()

class AppModel(Base):
    # 表的名字:
    __tablename__ = 'App'

    appId = Column(String, primary_key=True)
    appName = Column(String)
    appType = Column(String)
    appCreateTime = Column(DateTime)
    appDownLoadUrl = Column(String)
    appQRCodeUrl = Column(String)
    appLinkUrl = Column(String)
    userId = Column(String)
    runTime = Column(DateTime)
    runStatus = Column(String)

    def getDic(self):
        dic = self.__dict__
        dic.pop('_sa_instance_state')
        if (self.appCreateTime != None):
            dic['appCreateTime'] = self.appCreateTime.strftime('%Y-%m-%d %H:%M:%S')
        if (self.runTime != None):
            dic['runTime'] = self.runTime.strftime('%Y-%m-%d %H:%M:%S')

        return dic

    def getJson(self):

        dic = self.getDic()
        return JSONEncoder().encode(dic)


# 插入新的app
def insertApp(appName,appType,appLinkUrl,userId):

    session = getSession()
    appModelArray = session.query(AppModel).order_by(AppModel.appId).all()

    lastAppId = 0

    if (len(appModelArray) >= 1):
        lastApp = appModelArray[len(appModelArray) - 1]
        lastAppId = long(lastApp.appId)

    nextAppId = lastAppId + 1
    createTime = datetime.now()
    newAppModel = AppModel(
            appId=nextAppId,
            appName=appName,
            appType=appType,
            appLinkUrl=appLinkUrl,
            appCreateTime=createTime,
            userId=userId,
            runStatus='new',
    )

    session.add(newAppModel)
    session.commit()
    session.close()

    return (True,"App插入成功")

# insertApp("a222er","web","www.baidu.com","1")


# 获取某个用户的所有app
def getAppListByUserId(userId):

    session = getSession()
    appModelArray = session.query(AppModel).filter(AppModel.userId == userId).all()
    return appModelArray


# appList = getAppListByUserId('1')
# dd = []
# for a in appList:
#     dd.append(a.getDic())
# encodedjson = json.dumps(dd)
# print(encodedjson)