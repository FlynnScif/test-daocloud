#coding: UTF-8
import os
import sae
import web
from web.contrib.template import render_jinja

web.config.debug = True

class Createdb:

	#def __init__(self):


	def GET(self):
		self.app_root = os.path.dirname(__file__)
		self.templates_root = os.path.join(self.app_root,'templates')
		self.render = web.template.render(self.templates_root)
		return render.hellodb()