import webapp2
import logging

from handlers import site

app = webapp2.WSGIApplication([
		('/', site.Splash),
		(r'/[aA]bout/?', site.About),
		(r'/[cC]ontact/?', site.Contact),
		(r'/[uU]pload/?', site.UploadForm),
		(r'/upload_file', site.UploadHandler),
		(r'/[cC]atalog/?', site.Catalog),
		(r'/[cC]atalog/([^/]+)?', site.ViewNote),
		(r'/[sS]ettings/?', site.Settings),
	])

def handle_404(req, res, err):
	logging.exception(err)
	res.write("Sorry, something went wrong.")
	res.set_status(404)

app.error_handlers[404] = handle_404