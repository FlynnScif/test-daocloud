#coding: UTF-8
import os
import sae
import web
from web.contrib.template import render_jinja
#from mysqlcha import Createdb

web.config.debug = True

class Createdb:

	def __init__(self):
		self.app_root = os.path.dirname(__file__)
		self.templates_root = os.path.join(self.app_root,'templates')
		self.render = web.template.render(self.templates_root)

	def GET(self):
		return self.render.hellodb()
#		return render.index()
