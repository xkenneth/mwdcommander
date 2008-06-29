### GROK ###
import grok

grok.templatedir('app_templates')

### ZOPE ###
from persistent.list import PersistentList

### BOILERPLATE ###

class GenericContainer(grok.Container):
    def __init__(self):
        super(GenericContainer, self).__init__()
        self.item_count = 0
        self.item_order = PersistentList()

    def items(self):
        t = []
        for key in self.item_order: t.append(self[unicode(key)])
        return t

    def inverse_items(self):
        t = self.items()
        t.reverse()
        return t

class Index(grok.View):
    pass

def get_application(context):
    obj = context
    while not isinstance(obj, grok.Application):
        obj = obj.__parent__
    return obj
