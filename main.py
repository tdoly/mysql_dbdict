#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
File: main.py
Author: tdoly
Description: the main
'''

import os
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
import rpc_client as rc

from tornado.options import define, options

define("port", default=8000, help="run on the default port 8000", type=int)

class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r"/(\w*)",IndexHandler),
        ]
        settings = dict(
            template_path = self.paths("templates"),
            static_path = self.paths("static"),
            debug = True,
        )
        tornado.web.Application.__init__(self, handlers, **settings)

    def paths(self, filename):
        return os.path.join(os.path.dirname(__file__), filename)

class IndexHandler(tornado.web.RequestHandler):
    def get(self, select):
        dbs = rc.dbs()
        datas = {}
        currentDb = (select and [select] or dbs)[0]
        if dbs and currentDb in dbs:
            datas = rc.datas(currentDb)
        print datas
        self.render(
            "index.html",
            dbs = dbs,
            datas = datas,
            currentDb = currentDb,
        )

if __name__ == '__main__':
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(Application())
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()


