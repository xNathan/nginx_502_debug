import time
import random
import tornado.gen
import tornado.ioloop
import tornado.web
import tornado.httpserver

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        # Simulate a slow web server
        # time.sleep(0.002)
        arr = [random.random() for x in range(10000)]
        self.write("Hello, world")

def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
    ])

if __name__ == "__main__":
    app = make_app()
    server = tornado.httpserver.HTTPServer(app)
    server.bind(8888)
    server.start()
    tornado.ioloop.IOLoop.current().start()
