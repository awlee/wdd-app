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

<<<<<<< HEAD
class LoginHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("login.html")
=======
###########

class Score():
    def __init__(self):
        self.score = 0

    def addscore(self, addval):
        self.score = self.score + addval

    def resetScore(self, initscore):
        self.score = initscore

    def displayscore(self):
        print("Score: "+ str(self.score))
        #display the score

    def displayhigh(self,userid,game=""):
        #returns a list of [game score] pairs if game isn't specified, else returns score
        scorefile = open("scoresheet.txt","r")
        outp = []
        for line in scorefile:
                if(line.split())[0] == str(userid):
                        if (game == ""):
                                outp = outp + [[(line.split())[1], (line.split())[2]]]
                        elif (line.split())[1] == str(game):
                                outp = int((line.split())[2])
        return outp



    def storescore(self, userid, game, score):
        scorefile = open("scoresheet.txt", "r")
        highscore = False
        newscore = True
        linenum = 0
        scfile = []
        for i in scorefile:
                scfile = scfile + [i.replace("\n","")]

        for line in scfile:
            if (line.split())[0] == str(userid):
                print("userid is equal")
                if (line.split())[1] == game:
                        newscore = False
                        if int(line.split()[2]) < score:
                                scfile[linenum] = str(userid) + " "+ str(game) + " " + str(score)
                                highscore = True
                                break
            linenum = linenum + 1
        if newscore:
            scfile = scfile + [str(userid) + " " + str(game) + " " + str(score)]
        scorefile.close()

        if highscore or newscore:
            scorefile_w = open("scoresheet.txt", "w")
            for writeline in scfile:
                scorefile_w.write(writeline + "\n" )
            scorefile_w.close()
            

>>>>>>> 0e7acbf4573cd37adf65e780ccada71321e19664

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
