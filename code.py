# -*- coding: UTF-8 -*-
from controllers.login import *
from controllers.index import *
from controllers.register import *
from controllers.user import *
from controllers.error import *


# "使用https"
# from web.wsgiserver import CherryPyWSGIServer
# from web.wsgiserver.ssl_builtin import BuiltinSSLAdapter
# ssl_certificate = "/Users/apple/Desktop/Workspace/Python/openssl/key/cacert.pem"
# ssl_private_key = "/Users/apple/Desktop/Workspace/Python/openssl/key/prvtkey.pem"
# CherryPyWSGIServer.ssl_adapter = BuiltinSSLAdapter(ssl_certificate,ssl_private_key,None)

urls = (
    '/','index',
    '/index','index',
    '/login','login',
    '/register','register',
    '/identifyCode','identifyCode',
    '/user','user',
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


if __name__ == "__main__":
    app = web.application(urls,globals())
    app.notfound = notfound
    app.internalerror = internalerror
    app.run()