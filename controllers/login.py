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
        userPassword = postParams.get('userPassword')
        loginType = postParams.get('loginType')
        loginIp = web.ctx.ip
        print(u"get: userEmail:%s userPhoneNum:%s password:%s loginType:%s loginIp:%s"%(userEmail,userPhoneNum,userPassword,loginType,loginIp))

        userModel = None
        if(userEmail != None and userEmail != ""):
            userModel = getUserByEmail(userEmail)
        elif (userPhoneNum != None and userPhoneNum != ""):
            userModel = getUserByPhone(userPhoneNum)

        backJsonResult = BackResult(result="",errorCode=0,errorMsg="")
        if userModel == None:
            backJsonResult.setErrorMsg(errorMsg="账号错误")
        elif userModel.userPassWord != userPassword:
            backJsonResult.setErrorMsg(errorMsg="密码不正确")
        else:
            loginAccessToken = random_str(28)
            loginAccount=userEmail
            if userEmail == None:
                loginAccount=userPhoneNum
            insertLogin(userId=userModel.userId,
                        loginAccount=loginAccount,
                        loginPosition='hangzhou',
                        loginType=loginType,
                        loginAccessToken=loginAccessToken,
                        loginIp=loginIp)
            updateUser(userModel.userId,loginType,loginAccessToken)
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



