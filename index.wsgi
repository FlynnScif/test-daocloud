# coding: UTF-8
import os
import sae
import web
from web.contrib.template import render_jinja
from mysqlcha import Createdb

web.config.debug = True

urls = ("/","index",
		"/hello","hello",
		"/api","api",
		"/createdb","Createdb"
        )

app_root = os.path.dirname(__file__)
templates_root = os.path.join(app_root,'templates')
render = web.template.render(templates_root)


class index:
	def GET(self):
		return render.index(name = "Hello World")

class hello:
	def GET(self):
		return render.hello()

class api:
	def GET(self):
		return render.api()



app = web.application(urls,globals()).wsgifunc()        
application = sae.create_wsgi_app(app)



