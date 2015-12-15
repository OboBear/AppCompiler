# -*- coding: UTF-8 -*-
import web

from utils.orm.UserModel import User
from utils.orm.OrmUtil import *

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

        session = getSession()
        for userEmail,userPassWord in session.query(User.userEmail,User.userPassWord)\
                .filter(User.userEmail == account):
            if(userPassWord == password):
                return 'success';

            return '密码错误'
        session.close()

        # newUser = User('1',account,password,'1575775','nickName','m',12,'Hangzhou',loginType);
        # newUser = User(userAccount='1',userEmail=account,userPassWord=password,userPhoneNum='123',userNickName='2',userGender='f',userAge=1,userCity='ci',userAccessTokenForWeb='2')
        # session = getSession()
        ## 添加到session:
        # session.add(newUser)
        ## 提交即保存到数据库:
        # session.commit()
        ## 关闭session:
        # session.close()
        # return 'success'



