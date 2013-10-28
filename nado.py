import tornado.ioloop
import tornado.web
from tornado.web import StaticFileHandler
from views import index

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write(index.view())

static_path = 'static'

application = tornado.web.Application([ 
    (r'/', MainHandler), 
    (r'/static/(.*)', StaticFileHandler, {'path' : static_path})
], gzip=True, static_path='static')

if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()