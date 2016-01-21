# -*- coding: UTF-8 -*-

import web
import commands
from utils.json.JsonUtil import *
from utils.orm.AppModel import *
from utils.orm.UserModel import *

# import sys
# reload(sys)
# print sys.getdefaultencoding()
# sys.setdefaultencoding("utf-8")
# print sys.getdefaultencoding()

# app 相关 url
APP_URLS = (
    '/app/list','AppList',          #
    '/app/create','AppCreate',      # 创建app
    '/app/compile','AppCompile',    # 运行app
)

# curl -d "loginType=web&userAccessToken=pvChtoBGBZkbdhVwxOFsAYYLfKyp" "120.27.51.48:10086/app/list"
class AppList:
    def GET(self):
        return 'app get'

    def POST(self):
        postParams = web.input()
        loginType = postParams.get("loginType")
        userAccessToken = postParams.get("userAccessToken")
        print('userAccessToken:'+userAccessToken)
        if ( loginType == None or userAccessToken == None):
            return backError("参数不全")
        currentUser = getUserByAccessToken(userAccessToken=userAccessToken,
                                           loginType=loginType)
        if (currentUser == None):
            return backError("invalidate userAccessToken")

        appList = getAppListByUserId(currentUser.userId)
        return backSuccess(result=getPureArrayFromArray(appList))

# 创建
class AppCreate:
    def GET(self):
        result = u'创建app'+\
               u'loginType:用户登录类型  web android ios\n'+\
               u'userAccessToken:accessToken \n'+\
               u'appName:所要创建的app的名称 \n'+\
               u'appType:所要创建的app的类型 web local original\n'+\
               u'appLinkUrl:如果是web类型的app,其链接所指向的网络地址\n'+\
    u'测试:\n'+\
    u'curl -d "userAccessToken="wxOFsAYYLfKyp"&loginType=web&appName=MyApp&appType=web&appLinkUrl="http://m.baidu.com"" "localhost:8080/app/create"'

        return result.encode('gbk')

    def POST(self):

        postParams = web.input()

        loginType = postParams.get("loginType")
        userAccessToken = postParams.get("userAccessToken")
        appName = postParams.get("appName")
        appType = postParams.get("appType")
        appLinkUrl = postParams.get("appLinkUrl")
        print('userAccessToken:'+userAccessToken)
        if (appName == None or loginType == None or userAccessToken == None or appType == None):
            return backError("参数不全")

        currentUser = getUserByAccessToken(userAccessToken=userAccessToken,
                                           loginType=loginType)

        if (currentUser == None):
            return backError("invalidate userAccessToken")

        (flag,message,appModel) = insertApp(appName=appName,appType=appType,appLinkUrl=appLinkUrl,userId=currentUser.userId)

        return backSuccess(result="app create success")

# 运行
class AppCompile:
    def GET(self):

        return "AppCompile get"


    def POST(self):

        return "AppCompile Post"


# appList = getAppListByUserId('1')
# print(backSuccess(getPureArrayFromArray(appList)))
# print(getJsonArrayFromArray(appList))