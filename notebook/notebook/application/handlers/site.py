import os
import jinja2
import logging

env = jinja2.Environment(
	loader = jinja2.FileSystemLoader('templates')) # os.path.dirname(__file__)

import webapp2
import datetime

from google.appengine.ext import db
from google.appengine.api import users, mail

class Splash(webapp2.RequestHandler):
	def get(self):

		title="Home"

		user = users.get_current_user()
		if user:
			url = users.create_logout_url(self.request.uri)
		else:
			url = users.create_login_url(self.request.uri)

		template_values = {
			'user': user,
			'login_url': url,
			'title': title,
		}

		template = env.get_template('splash.jinja')
		self.response.out.write(template.render(template_values))

class About(webapp2.RequestHandler):
	def get(self):

		title="About"

		user = users.get_current_user()
		if user:
			url = users.create_logout_url(self.request.uri)
		else:
			url = users.create_login_url(self.request.uri)

		template_values = {
			'user': user,
			'login_url': url,
			'title': title,
		}

		template = env.get_template('about.jinja')
		self.response.out.write(template.render(template_values))

class Contact(webapp2.RequestHandler):
	def get(self):
		
		title="Contact"

		user = users.get_current_user()
		if user:
			url = users.create_logout_url(self.request.uri)
		else:
			url = users.create_login_url(self.request.uri)

		template_values = {
			'user': user,
			'login_url': url,
			'title': title,
		}

		template = env.get_template('contact.jinja')
		self.response.out.write(template.render(template_values))

	def post(self):
		user = users.get_current_user()

		_name = self.request.get('name')
		_message = self.request.get('message')
		if user:
			_from = user.email()
		else:
			_from = self.request.get('email')

		message         = mail.EmailMessage()
		message.subject = "Notebook: Contact form from %s" % _from
		message.sender  = _from
		message.to      = "evantegl@gmail.com"
		message.body    = _message

		message.send()

		self.redirect('/')

class Upload(webapp2.RequestHandler):
	def get(self):

		title = "Upload"

		user = users.get_current_user()
		url  = users.create_logout_url(self.request.uri)

		template_values = {
			'user': user,
			'login_url': url,
			'title': title,
		}

		template = env.get_template('upload.jinja')
		self.response.out.write(template.render(template_values))

	def post(self):
		user = users.get_current_user()

		course = self.request.get('course')
		month  = self.request.get('month')
		day    = self.request.get('day')
		year   = self.request.get('year')

		self.redirect('/catalog')

class Catalog(webapp2.RequestHandler):
	def get(self):
		self.redirect('/upload')

class Settings(webapp2.RequestHandler):
	def get(self):
		self.redirect('/')