# -*- coding: UTF-8 -*-
import web

class index:
    def GET(self):
        render = web.template.render('templates/demo')
        return render.index()

