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
        account = postParams.get('account')
        password = postParams.get('password')
        loginType = postParams.get('type')
        print(account+":"+password+":"+loginType)

        (userModel,loginResult) = getUserByEmailAndPassword(account,password)

        if userModel==None:
            return loginResult

        loginAccessToken = random_str(16)
        insertLogin(userModel.userAccount,'hangzhou',loginType,loginAccessToken)
        updateUser(userModel.userAccount,loginType,loginAccessToken)
        return 'success'

class autoLogin:
    def GET(self):
        render = web.template.render('templates/demo')
        return render.login()
    def POST(self):
        postParams = web.input()
        loginAccessToken = postParams.get('loginAccessToken')
        loginType = postParams.get('type')



