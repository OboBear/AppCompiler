# -*- coding: UTF-8 -*-
import web
import commands

APP_URLS = ('/app','AppController',)

class AppController:
    def GET(self):
        return 'app'
    def POST(self):

        return ''