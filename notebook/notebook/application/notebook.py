import webapp2
import logging

# import jinja2
# jinja_environment = jinja2.Environment(
# 	loader = jinja2.FileSystemLoader('templates')) # os.path.dirname(__file__)

from handlers import site

app = webapp2.WSGIApplication([
	('/', site.Splash),
	('/about', site.About),
	('/contact', site.Contact)
	])

def handle_404(req, res, err):
	logging.exception(err)
	# res.write(jinja_environment.get_template('error.jinja'))
	res.write("Sorry, something went wrong.")
	res.set_status(404)

app.error_handlers[404] = handle_404