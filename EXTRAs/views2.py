import os

from twisted.application import internet
from twisted.web.resource import Resource
from twisted.web import server
from twisted.web.template import Element, renderer, XMLFile, tags, flatten
from twisted.python.filepath import FilePath

#from twisted.internet import reactor



class ThreadResource(Resource):
    def __init__(self, element):
        self.element = element
        Resource.__init__(self)

    def getChild(self, name, request):
        return self

    def render_GET(self, request):
        d = flatten(request, self.element, request.write)
        template_name = "template.xml"
#        element = self.loader.load(template_name)

        def cb(content):
            request.write(content)
            request.setResponseCode(200)
            request.finish()

        d = element.render(template_name)
        d.addCallback(cb)
        return server.NOT_DONE_YET


"""
#from twisted.web.template import Element, renderer, XMLFile, tags
#from twisted.python.filepath import FilePath

class ExampleElement(Element):
    loader = XMLFile(FilePath('template-1.xml'))

    @renderer
    def header(self, request, tag):
        return tag(tags.p('Header.'), id='header')

    @renderer
    def footer(self, request, tag):
        return tag(tags.p('Footer.'), id='footer')
"""
"""
from twisted.web.resource import Resource
from twisted.web.template import flatten
from twisted.web.server import NOT_DONE_YET

class ElementResource(Resource):
    def __init__(self, element):
        Resource.__init__(self)
        self.element = element

    def render_GET(self, request):
        d = flatten(request, self.element, request.write)
        def done(ignored):
            request.finish()
            return ignored
        d.addBoth(done)
        return NOT_DONE_YET
"""