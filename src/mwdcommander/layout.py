import grok

from zope.interface import Interface

### APP ###
from viewletmanagers import Navigation

### VIEWLETS ###
class Nav(grok.Viewlet):
    grok.viewletmanager(Navigation)
    grok.context(Interface)
