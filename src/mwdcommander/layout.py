import grok

from zope.interface import Interface

### APP ###
from viewletmanagers import Navigation, MainContent

### VIEWLETS ###
class Nav(grok.Viewlet):
    grok.viewletmanager(Navigation)
    grok.context(Interface)
    grok.order(1)

class Title(grok.Viewlet):
    grok.viewletmanager(Navigation)
    grok.context(Interface)
    grok.order(0)


