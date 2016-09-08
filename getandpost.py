import web
from web.contrib.template improt render_jinja

web.config.debug = True

class Postdm:

	def __init__(self):
		self.app_root = os.path.dirname(__file__)
		self.templates_root = os.path.join(self.app_root,'templates')
		self.render = web.template.render(self.templates_root)

	def __post(self):
		i = web.input()
		name = i.get('name')
		return '',name


class Getdm:

	pass
