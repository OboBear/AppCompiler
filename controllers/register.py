# -*- coding: UTF-8 -*-
import web
from utils.orm.RegisterUserModel import *
from utils.orm.UserModel import *
from utils.json.JsonUtil import *


class register:

    def GET(self):
        render = web.template.render('templates/demo')
        return render.register()

    def POST(self):
        postParams = web.input()
        userPhoneNum = postParams.get('userPhoneNum')
        password = postParams.get('userPassWord')
        identifyCode=postParams.get('identifyCode')
        userIdentifyCode = getRegisterIdentifyCode(userPhoneNum)
        if userIdentifyCode == None:
            return BackResult().setErrorMsg("请重新获取验证码").getJson()
        if userIdentifyCode != identifyCode:
            return BackResult().setErrorMsg("请重新获取验证码").getJson()
        (insterFlag,errorMsg)=insertUser(userPhoneNum=userPhoneNum,userPassWord=password)
        if insterFlag==False:
            result=JsonBaseClass()
            result.result=errorMsg
            return BackResult().setErrorMsg(result).getJson()
        result=JsonBaseClass()
        result.result="用户注册成功"
        return BackResult().setSuccessResult(result).getJson()

class identifyCode:
    def POST(self):
        postParams = web.input()
        userPhoneNum = postParams.get('userPhoneNum')
        result = JsonBaseClass()
        result.identify=insertRegister(userPhoneNum)
        backResult=BackResult(result)
        return backResult.getJson()
# print(getRegisterIdentifyCode(15757115391))