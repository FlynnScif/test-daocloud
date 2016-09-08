#coding: UTF-8
import os
import sae
import web
from web.contrib.template import render_jinja

web.config.debug = True

class Createdb:

	def __init__(self):
		app_root = os.path.dirname(__file__)
		templates_root = os.path.join(app_root,'templates')
		render = web.template.render(templates_root)

	def GET(self):
		return render.hellodb()