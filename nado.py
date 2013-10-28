import tornado.ioloop
import tornado.web
from views import index

class MainHandler(tornado.web.RequestHandler):
	def get(self):
		self.write(index.view())

application = tornado.web.Application([ (r'/', MainHandler), ])

if __name__ == "__main__":
	application.listen(8888)
	tornado.ioloop.IOLoop.instance().start()