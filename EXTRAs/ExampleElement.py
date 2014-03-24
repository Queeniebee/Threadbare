import os

from twisted.application import internet
from twisted.web.resource import Resource
from twisted.web import server
from twisted.web.template import Element, renderer, XMLFile, tags, flatten
from twisted.python.filepath import FilePath

class ExampleElement(Element):
    loader = XMLFile(FilePath('template.xml'))

    @renderer
    def header(self, request, tag):
        return tag(tags.p('Templated content.'), id='content')

    @renderer
    def footer(self, request, tag):
        return tag(tags.p('[1, 2, 3, 4, 5, 6].'), id='extra_info')