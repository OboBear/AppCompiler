# -*- coding: UTF-8 -*-
import web

from utils.orm.UserModel import *
from utils.orm.LoginModel import *
from utils.util import *
from utils.orm.OrmUtil import *
from utils.json.JsonUtil import *

class login:
    def GET(self):

        render = web.template.render('templates/demo')
        return render.login()

    def POST(self):
        postParams = web.input()
        userEmail = postParams.get('userEmail')
        userPhoneNum = postParams.get('userPhoneNum')
        password = postParams.get('password')
        loginType = postParams.get('type')
        print(u"get: userEmail:%s userPhoneNum:%s password:%s loginType:%s"%(userEmail,userPhoneNum,password,loginType))

        userModel = None
        if(userEmail != None and userEmail != ""):
            userModel = getUserByEmail(userEmail)
        elif (userPhoneNum != None and userPhoneNum != ""):
            userModel = getUserByPhone(userPhoneNum)

        backJsonResult = BackResult(result="",errorCode=0,errorMsg="")
        if userModel == None:
            backJsonResult.setErrorMsg(errorMsg="账号错误")
        elif userModel.userPassWord != password:
            backJsonResult.setErrorMsg(errorMsg="密码不正确")
        else:
            loginAccessToken = random_str(28)
            loginAccount=userEmail
            if userEmail == None:
                loginAccount=userPhoneNum
            insertLogin(userAccount=userModel.userAccount,
                        loginAccount=loginAccount,
                        loginPosition='hangzhou',
                        loginType=loginType,
                        loginAccessToken=loginAccessToken)
            updateUser(userModel.userAccount,loginType,loginAccessToken)
            backResult=JsonBaseClass()
            backResult.loginAccessToken=loginAccessToken
            backJsonResult.result=backResult

        return backJsonResult.getJson()

class autoLogin:
    def GET(self):
        render = web.template.render('templates/demo')
        return render.login()
    def POST(self):
        postParams = web.input()
        loginAccessToken = postParams.get('loginAccessToken')
        loginType = postParams.get('type')



