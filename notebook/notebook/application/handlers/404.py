import webapp2
import jinja2
import logging
jinja_environment = jinja2.Environment(
	loader = jinja2.FileSystemLoader('templates')) # os.path.dirname(__file__)
from google.appengine.api import users

class Error(webapp2.RequestHandler):
	def get(self):
		template = jinja_environment.get_template('error.jinja')

		user = users.get_current_user()

		if user:
			url = users.create_logout_url(self.request.uri)
		else:
			url = users.create_login_url(self.request.uri)

		template_values = {
			'user': user,
			'login_url': url,
		}

		template = jinja_environment.get_template('error.jinja')
		self.response.out.write(template.render(template_values))

app = webapp2.WSGIApplication([(r'/.*', Error)])