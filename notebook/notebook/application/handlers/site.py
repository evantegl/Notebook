import os
import urllib
import jinja2
import logging

env = jinja2.Environment(
	loader = jinja2.FileSystemLoader('templates')) # os.path.dirname(__file__)

import webapp2
import datetime

from google.appengine.ext import db, blobstore
from google.appengine.api import users, mail
from google.appengine.ext.webapp import blobstore_handlers

##### Custom functions #####
############################


##### Custom classes #####
##########################

class Note(db.Model):
	course        = db.StringProperty()
	recorded_date = db.DateProperty()
	upload_date   = db.DateProperty(auto_now_add=True)
	user          = db.UserProperty(auto_current_user_add=True)
	data_key      = blobstore.BlobReferenceProperty()

##### Request handlers #####
############################

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

	user = users.get_current_user()
	
	def get(self):
		
		title="Contact"

		if self.user:
			url = users.create_logout_url(self.request.uri)
		else:
			url = users.create_login_url(self.request.uri)

		template_values = {
			'user': self.user,
			'login_url': url,
			'title': title,
		}

		template = env.get_template('contact.jinja')
		self.response.out.write(template.render(template_values))

	def post(self):
	
		_name = self.request.get('name')
		_message = self.request.get('message')
		if user:
			_from = self.user.email()
		else:
			_from = self.request.get('email')

		message         = mail.EmailMessage()
		message.subject = "Notebook: Contact form from %s" % _from
		message.sender  = _from
		message.to      = "evantegl@gmail.com"
		message.body    = _message

		message.send()

		self.redirect('/')

class UploadForm(webapp2.RequestHandler):
	
	user = users.get_current_user()
	
	def get(self):

		title = "Upload"
		url  = users.create_logout_url(self.request.uri)

		template_values = {
			'user': self.user,
			'login_url': url,
			'title': title,
			'upload_url': blobstore.create_upload_url('/upload_file')
		}

		template = env.get_template('upload.jinja')
		self.response.out.write(template.render(template_values))

class UploadHandler(blobstore_handlers.BlobstoreUploadHandler):
	def post(self):

		course = self.request.get('course')
		year   = self.request.get('year')
		month  = self.request.get('month')
		day    = self.request.get('day')
		data   = self.get_uploads('file')

		data_key = data[0].key()

		note               = Note()
		note.course        = course
		note.recorded_date = datetime.date(int(year), int(month), int(day))
		note.data_key      = data_key

		note.put()

		self.redirect('/catalog/%s' % data_key)
		# self.redirect('/')

class ViewNote(blobstore_handlers.BlobstoreDownloadHandler):
	def get(self, note_key):
		note_key = str(urllib.unquote(note_key))
		info = blobstore.BlobInfo.get(note_key)
		self.send_blob(info)

class Catalog(webapp2.RequestHandler):
	
	user = users.get_current_user()
	
	def get(self):
		self.redirect('/')

class Settings(webapp2.RequestHandler):
	
	user = users.get_current_user()
	
	def get(self):
		self.redirect('/')