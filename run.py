import os
import sys


from twisted.application import internet
from twisted.web import server
from twisted.internet import reactor
from views import *
from twisted.web.static import File
from twisted.python.util import sibpath

"""root = Resource()
root.putChild("static", File(sibpath(__file__, "static")))
"""

TEMPLATE_DIR = sibpath(__file__, 'Threadbare')
site = server.Site(ThreadResource())
reactor.listenTCP(8000, site)
reactor.run()