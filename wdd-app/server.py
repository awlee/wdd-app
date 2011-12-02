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
        scorefile = open("scoresheet.txt", "r")
        highscore = False
        newscore = False
        linenum = 0
        for line in scorefile:
            if ((line.toString()).split())[0] == userid.toString():
                if ((line.toString()).split())[1] == game:
                        newscore = True
                    if int(((line.toString()).split())[2]) < score
                        scfile = scfile.getlines()
                        scfile[linenum] = userid + " "+ game + " " + score + "\n"
                        highscore = True
                        break
            linenum = linenum + 1
        
        
        
        if highscore == 1:
            scorefile_w = open("scoresheet.txt", "w")
            
        
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
