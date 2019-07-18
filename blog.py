import webapp2
import jinja2
import os

jinja_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class HomePage(webapp2.RequestHandler):
    def get(self):
        template= jinja_env.get_template("blogasaurus.html")
        self.response.headers['content-type'] = 'text/html'
        self.response.write(template.render())


class Cecille(webapp2.RequestHandler):
    def get(self):
        template= jinja_env.get_template("cecille.html")





app = webapp2.WSGIApplication([
    ("/home", HomePage),
    ("/cecille", Cecille)

], debug=True)
