import tornado.ioloop
import tornado.web

from bradoc import Bradoc

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write(Bradoc().render())

application = tornado.web.Application([
    (r"/", MainHandler),
])

if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()

from bradoc import Bradoc
from dominate.html.tags import *

from views.index import Views
