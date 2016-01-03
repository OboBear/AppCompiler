# -*- coding: UTF-8 -*-
import web

from utils.orm.UserModel import *
from utils.json.JsonUtil import *

USER_URLS = ('/user','user',)

class user:
    def POST(self):
        postParams=web.input()
        userAccessToken=postParams.get('userAccessToken')
        loginType = postParams.get('loginType')
        user = getUserByAccessToken(userAccessToken,loginType)
        if (user == None):
            return BackResult().setErrorMsg("无效token,请重新登录")

        result = JsonBaseClass()
        result.userInfo.userEmail=user.userEmail
        result.userInfo.userPhoneNum=user.userPhoneNum
        result.userInfo.userNickName=user.userNickName
        result.userInfo.userGender=user.userGender
        result.userInfo.userAge=user.userAge
        result.userInfo.userCity=user.userCity
        result.userInfo.userRegisterTime=(u"%s"%user.userRegisterTime)
        backRsultJson = BackResult().setSuccessResult(result)
        return backRsultJson

