import tornado.ioloop
import tornado.web
import tornado.template
###import tornado.database
import os

###class BaseHandler(tornado.web.RequestHandler):
    ###def get_current_user(self):
"""user_json=self.get_cookie("user")
if user_json:
name = tornado.escape.json_decode(user_json)
db = tornado.database.Connection("localhost", "wdd", "root") 
user = db.get("SELECT * FROM user WHERE name= '" + name + "';")
db.close()
return user
else:
return None
"""
###class BaseHandler
imgsrc = ""    
class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("index.html")

class LoginHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("login.html")

class FooterHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("footer.html")
class GameHandler(tornado.web.RequestHandler):
      def get_template_path(self):
        """Override to customize template path for each handler.
        By default, we use the 'template_path' application setting.
        Return None to load templates relative to the calling file.
        """
        return self.application.settings.get("game_path")
      def get(self):
        self.render("concentration.html")
  
application = tornado.web.Application([

        # WDD TODO
        # Add more route(s) to handle the doubling
        
 (r"/",MainHandler),
 (r"/login",LoginHandler),
 (r"/footer", FooterHandler),
 (r"/games",GameHandler)
   ###### routes end here ######

#########################
# Don't change this     #
#########################
], debug=True,
  template_path=os.path.join(os.path.dirname(__file__), "templates"),
  static_path=os.path.join(os.path.dirname(__file__), "static"),
  game_path=os.path.join(os.path.dirname(__file__), "game"),                              

)

if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
