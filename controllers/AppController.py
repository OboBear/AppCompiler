# -*- coding: UTF-8 -*-
import web

APP_URLS = ('/app','AppController',)

class AppController:
    def GET(self):
        return 'app';
