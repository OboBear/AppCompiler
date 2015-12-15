# -*- coding: UTF-8 -*-
import web

#404 error
def notfound():
    render=web.template.render('templates/error')
    return web.notfound(render.error404())

#500 error
def internalerror():
    render=web.template.render('templates/error')
    return web.notfound(render.error500())