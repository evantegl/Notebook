import os
import jinja2
import logging

jinja_environment = jinja2.Environment(
	loader = jinja2.FileSystemLoader('templates')) # os.path.dirname(__file__)

import webapp2
import datetime

from google.appengine.ext import db
from google.appengine.api import users, mail

class Splash(webapp2.RequestHandler):
	def get(self):

		_user = users.get_current_user()
		if _user:
			url = users.create_logout_url(self.request.uri)
		else:
			url = users.create_login_url(self.request.uri)

		template_values = {
			'user': _user,
			'login_url': url
		}

		template = jinja_environment.get_template('splash.jinja')
		self.response.out.write(template.render(template_values))

class About(webapp2.RequestHandler):
	def get(self):

		_user = users.get_current_user()
		if _user:
			url = users.create_logout_url(self.request.uri)
		else:
			url = users.create_login_url(self.request.uri)

		template_values = {
			'user': _user,
			'login_url': url
		}

		template = jinja_environment.get_template('about.jinja')
		self.response.out.write(template.render(template_values))

class Contact(webapp2.RequestHandler):
	def get(self):

		_user = users.get_current_user()
		if _user:
			url = users.create_logout_url(self.request.uri)
		else:
			url = users.create_login_url(self.request.uri)

		template_values = {
			'user': _user,
			'login_url': url
		}

		template = jinja_environment.get_template('contact.jinja')
		self.response.out.write(template.render(template_values))

	def post(self):
		user = users.get_current_user()
		# if _user:
		# 	url = users.create_logout_url(self.request.uri)
		# else:
		# 	url = users.create_login_url(self.request.uri)

		# template_values = {
		# 	'user': _user,
		# 	'login_url': url
		# }
		# template=jinja_environment.get_template('contact.jinja')

		_name = self.request.get('name')
		_message = self.request.get('message')
		if user:
			_from = user.email()
		else:
			_from = self.request.get('email')

		message = mail.EmailMessage()
		message.subject = "Notebook: Contact form from %s" % _from
		message.sender = _from
		message.to = "evantegl@gmail.com"
		message.body = _message

		message.send()

		self.redirect('/')