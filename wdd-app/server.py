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
class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("index.html")

###########
score = 0

class Score():
    def addscore(addval):
        score = score + addval
    def resetScore(initscore):
        score = initscore
    def displayscore(score):
        
    def storescore(score, game, userid):
        scorefile = open("/public_html/mp1/scoresheet.txt", "w")
        highscore = 0
        for line in scorefile:
            if ((line.toString()).split())[0] == userid:
                if ((line.toString()).split())[1] == game:
                    if int(((line.toString()).split())[2]) < score
                        line.
                        scorefile.write(userid + " "+ game + " " + score\n)
                        highscore = 1
        if highscore == 1:
            #Display Congratulations high score is
        


application = tornado.web.Application([

  # WDD TODO
  # Add more route(s) to handle the doubling

  (r"/",       MainHandler),

  ###### routes end here ######

#########################
# Don't change this     #
#########################
], debug=True,
   template_path=os.path.join(os.path.dirname(__file__), "templates"),
   static_path=os.path.join(os.path.dirname(__file__), "static"),
)

if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
