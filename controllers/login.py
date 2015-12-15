# -*- coding: UTF-8 -*-
import web
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
        return 'success'



