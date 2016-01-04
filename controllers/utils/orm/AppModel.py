# -*- coding: UTF-8 -*-

from sqlalchemy import Column, String,Integer,DateTime,create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from OrmUtil import *
from datetime import *

# 创建对象的基类:
Base = declarative_base()

class AppModel(Base):
    # 表的名字:
    __tablename__ = 'App'

    appId = Column(String, primary_key=True)
    appName = Column(String)
    appType = Column(DateTime)
    appDownLoadUrl = Column(String)
    appQRCode = Column(String)
    appLinkUrl = Column(String)
    userId = Column(String)


