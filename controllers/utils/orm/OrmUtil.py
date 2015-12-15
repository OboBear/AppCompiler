# -*- coding: UTF-8 -*-
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

def getSession():
    # 初始化数据库连接:
    engine = create_engine('mysql+mysqlconnector://obo:12341234a@120.27.51.48:3306/AppBuilder')
    # 创建DBSession类型:
    DBSession = sessionmaker(bind=engine)
    ## 创建session对象:
    session = DBSession()
    return session
