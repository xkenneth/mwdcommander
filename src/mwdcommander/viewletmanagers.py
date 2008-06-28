import grok

### ZOPE ###
from zope.interface import Interface

class Navigation(grok.ViewletManager):
    grok.name('navigation')
    grok.context(Interface)
