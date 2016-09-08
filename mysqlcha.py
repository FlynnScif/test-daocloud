#coding: UTF-8
import os
import sae
import web
from web.contrib.template import render_jinja
import sae.const 
#from mysqlcha import Createdb

web.config.debug = True
#db = web.database(dbn='mysql',port=int(sae.const.MYSQL_PORT),host=sae.const.MYSQL_HOST,user=sae.const.MYSQL_USER,pw=sae.const.MYSQL_PASS,db='app_yzjapi')
db = web.database(dbn='mysql',port='3307',host=w.rdc.sae.sina.com.cn ,user=45m4jo5z33,pw=hl3mj5kim1j0l0iyxyl4524z2mj5055y1xw53yyk,db='app_yzjapi')


class Createdb:

	def __init__(self):
		self.app_root = os.path.dirname(__file__)
		self.templates_root = os.path.join(self.app_root,'templates')
		self.render = web.template.render(self.templates_root)

	def GET(self):
		todos = db.select('todo')
		return self.render.hellodb(todos)
#		return self.render.hellodb()
#		return render.index()
