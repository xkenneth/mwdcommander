import grok

### ZOPE ###
from zope.interface import Interface

class Head(grok.ViewletManager):
    grok.name('head')
    grok.context(Interface)

class Navigation(grok.ViewletManager):
    grok.name('navigation')
    grok.context(Interface)

class MainContent(grok.ViewletManager):
    grok.name('content')
    grok.context(Interface)

class SideContent(grok.ViewletManager):
    grok.name('left')
    grok.context(Interface)
