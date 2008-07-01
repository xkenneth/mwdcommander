import grok
import pdb

from zope.interface import Interface

### APP ###
from viewletmanagers import Navigation, MainContent, Head

### VIEWLETS ###
class Nav(grok.Viewlet):
    grok.viewletmanager(Navigation)
    grok.context(Interface)
    grok.order(2)

class Title(grok.Viewlet):
    grok.viewletmanager(Navigation)
    grok.context(Interface)
    grok.order(1)

