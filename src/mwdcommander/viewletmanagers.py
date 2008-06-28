import grok

### ZOPE ###
from zope.interface import Interface

class Navigation(grok.ViewletManager):
    grok.name('navigation')
    grok.context(Interface)

class MainContent(grok.ViewletManager):
    grok.name('content')
    grok.context(Interface)
