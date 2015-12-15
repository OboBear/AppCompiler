# -*- coding: UTF-8 -*-
from controllers.login import *
from controllers.index import *
from controllers.error import *

urls = (
    '/','index',
    '/index','index',
    '/login','login'
)

if __name__ == "__main__":
    app = web.application(urls,globals())
    app.notfound = notfound
    app.internalerror = internalerror;
    app.run()