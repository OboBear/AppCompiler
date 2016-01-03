# -*- coding: UTF-8 -*-
from controllers.LoginController import *
from controllers.index import *
from controllers.RegisterController import *
from controllers.UserController import *
from controllers.ErrorController import *
from controllers.AppController import *


# "使用https"
# from web.wsgiserver import CherryPyWSGIServer
# from web.wsgiserver.ssl_builtin import BuiltinSSLAdapter
# ssl_certificate = "/Users/apple/Desktop/Workspace/Python/openssl/key/cacert.pem"
# ssl_private_key = "/Users/apple/Desktop/Workspace/Python/openssl/key/prvtkey.pem"
# CherryPyWSGIServer.ssl_adapter = BuiltinSSLAdapter(ssl_certificate,ssl_private_key,None)

urls = (
    '/','index',
    '/index','index',
    # '/testJson','testJson'
)


# class testJson:
#     def GET(self):
#         user = getUserByAccount('1')
#         jsonBack = BackResult()
#         result = JsonBaseClass()
#         result.userAccount=user.userAccount
#         result.useruserName=user.userNickName
#         jsonBack.result=result
#         return jsonBack.getJson()
#
#     def POST(self):
#         postParams = web.input()
#         Result = postParams.get('Result')
#         print(Result)

def getUrls():

    targetUrl = urls

    # 登录相关
    targetUrl += LOGIN_URLS
    # 注册相关
    targetUrl += REGISTER_URLS
    # 用户相关
    targetUrl += USER_URLS
    # App相关
    targetUrl += APP_URLS

    return targetUrl


if __name__ == "__main__":
    app = web.application(getUrls(),globals())
    app.notfound = notfound
    app.internalerror = internalerror
    app.run()