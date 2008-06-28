import grok

### ZOPE ###
from zope.interface import Interface
from zope.schema import TextLine
from persistent.list import PersistentList

grok.templatedir('app_templates')

class IPipeTallyLog(Interface):
    name = TextLine(title=u"Name:")

class PipeTallyLog(grok.Container):

    grok.implements(IPipeTallyLog)

    def __init__(self, name):
	super(PipeTallyLog, self).__init__()
        self.name = name
	self.tally_count = 0
	self.tally_order = PersistentList()

class Index(grok.View):
    pass

            
