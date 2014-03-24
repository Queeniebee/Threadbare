import os

from twisted.application import internet
from twisted.web.resource import Resource
from twisted.web import server
from twisted.internet import reactor
from twisted.web.template import Element, renderer, XMLFile, tags, renderElement
from twisted.python.filepath import FilePath
from twisted.python.util import sibpath
from twisted.web.static import File

class ElementResource(Resource):
    def __init__(self, element):
        Resource.__init__(self)
        self.element = element

    def render_GET(self, request):
        return renderElement(request, self.element)

class ExampleElement(Element):
    loader = XMLFile(FilePath('threadbare.html'))

    @renderer
    def header(self, request, tag):
        return tag(tags.p('Templated content.'), id='content')

    @renderer
    def footer(self, request, tag):
        return tag(tags.p('[1, 2, 3, 4, 5, 6].'), id='extra_info')

class MyElement(Element):
     loader = XMLFile(FilePath('template2.xml'))

     @renderer
     def header(self, request, tag):
         return tag(tags.p('This is very different'), id='more_info')
     @renderer
     def body(self, request, tag):
         return tag(tags.p('So very different'), id='content')


class ThreadResource(Resource):
    def getChild(self, name, request):
        if name == 'template2':
           return ElementResource(ExampleElement())
        if name == 'template3':
           return ElementResource(MyElement())
        return self
     
    def render_GET(self, request):
        return 'loader'

root = ThreadResource()
site = server.Site(root)
reactor.listenTCP(8000, site)
reactor.run()

"""from twisted.application import internet
from twisted.web.resource import Resource
from twisted.web import server
from twisted.web.template import Element, renderer, XMLFile, tags, renderElement
from twisted.python.filepath import FilePath

#from twisted.internet import reactor

class ElementResource(Resource):
    def __init__(self, element):
        Resource.__init__(self)
        self.element = element

    def render_GET(self, request):
        return renderElement(request, self.element)

class ExampleElement(Element):
    loader = XMLFile(FilePath('template.xml'))

    @renderer
    def header(self, request, tag):
        return tag(tags.p('Templated content.'), id='content')

    @renderer
    def extra_info(self, request, tag):
        return tag(tags.p('[1, 2, 3, 4, 5, 6].'), id='extra_info')

class ThreadResource(Resource):
    def getChild(self, name, request):
        if name == 'foo':
           return ElementResource(ExampleElement())
        return self

    def render_GET(self, request):
        return 'Nope'"""
