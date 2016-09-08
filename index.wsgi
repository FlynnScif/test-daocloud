# coding: UTF-8
import os
import sae
import web
from web.contrib.template import render_jinja

urls = ("/","index",
		"/hello","hello"
        )

app_root = os.path.dirname(__file__)
templates_root = os.path.join(app_root,'templates')
render = web.template.render(templates_root)


class index:
	def GET(self):
		return render.index()

class hello:
	def GET(self):
		return render.hello()



app = web.application(urls,globals()).wsgifunc()        
application = sae.create_wsgi_app(app)



