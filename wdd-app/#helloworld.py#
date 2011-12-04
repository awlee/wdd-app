"""
A Tornado web application maps URLs or URL patterns to subclasses of tornado.web.RequestHandler. Those classes define get() or post() methods to handle HTTP GET or POST requests to that URL.
"""
import tornado.ioloop 
import tornado.web

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world")
application = tornado.web.Application([
        (r"/", MainHandler),
])
if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
