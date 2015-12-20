# -*- coding: UTF-8 -*-
import web

class register:

    def GET(self):
        render = web.template.render('templates/demo')
        return render.register()

    def POST(self):
        postParams = web.input()
        account = postParams.get('account')
        password = postParams.get('password')
        identifyCode=postParams.get('identifyCode')

class identifyCode:
    def POST(self):
        postParams = web.input()
        postParams.get('account')

