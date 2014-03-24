import os

from twisted.application import internet
from twisted.web import resource
from twisted.internet import reactor
from twisted.web import server
#from jinja2 import Environment, FileSystemLoader

import txtemplate


#jinja = Environment(loader=FileSystemLoader("templates"))

TEMPLATE_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../templates")

class HelloWorld(resource.Resource):
    def __init__(self):
        resource.Resource.__init__(self)
        self.loader = txtemplate.Jinja2TemplateLoader(TEMPLATE_DIR)

    def getChild(self, name, request):
        return self

    def render_GET(self, request):
        template_name = "template.html"
        template = self.loader.load(template_name)
        context = {'content': "Templated content", 'extra_info': [1, 2, 3, 4, 5, 6]}

        def cb(content):
            request.write(content)
            request.setResponseCode(200)
            request.finish()

        d = template.render(**context)
        d.addCallback(cb)
        return server.NOT_DONE_YET


site = server.Site(HelloWorld())
reactor.listenTCP(8888, site)
reactor.run()