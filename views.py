import os

from twisted.application import internet
from twisted.web.resource import Resource
from twisted.web import server
from twisted.internet import reactor
from twisted.python.util import sibpath
from twisted.web.static import File

import txtemplate

TEMPLATE_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "templates")
"""
class MainResource(Resource):
    def __init__(self, page):
        Resource.__init__(self)
        self.loader = txtemplate.Jinja2TemplateLoader(TEMPLATE_DIR)
        self.page = page

    def render_GET(self, request):
        page_name = "template.html"
        tmplate = self.loader.load(page_name)
        return tmplate
"""
class ThreadResource(Resource):
    def __init__(self):
        Resource.__init__(self)
        self.loader = txtemplate.Jinja2TemplateLoader(TEMPLATE_DIR)

    def getChild(self, name, request):
        if name == '':
            return self
        if name == 'threadbare':
            return MainResource(page)

    def render_GET(self, request):
        page_name = "threadbare.html"
        template = self.loader.load(page_name)
        context = {'greeting': "Enter", 'letter': "I'm so happy you're here."}

        def cb(content):
            request.write(content)
            request.setResponseCode(200)
            request.finish()
        d = tmplate.render(context)
        d.addCallback(cb)
        return server.NOT_DONE_YET

class BareResource(Resource):
    def getChild(self, name, request):
        if name == 'page2':
            return self

    def render_GET(self, request):
        template_name = "page2.html"
        template = self.loader.load(template_name)
        context = {'greeting': "Hey, YOU.", 'letter': "Did you say 'Hello' to her?"}

        def cb(content):
            request.write(content)
            request.setResponseCode(200)
            request.finish()

        d = template.render()
        d.addCallback(cb)
        return server.NOT_DONE_YET

root = ThreadResource()
root.putChild("static", File("static"))
root.putChild("threadbare", File("/templates"))
root.putChild("page3", File("/templates"))
root.putChild("page2", File("/templates"))
root.putChild("template", File("/templates"))


site = server.Site(root)
reactor.listenTCP(8000, site)
reactor.run()