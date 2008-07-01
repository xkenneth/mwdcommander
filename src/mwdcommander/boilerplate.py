### GROK ###
import grok
import pdb

grok.templatedir('app_templates')

### APP ###
from viewletmanagers import MainContent

### ZOPE ###
from persistent.list import PersistentList

### BOILERPLATE ###

class GenericContainer(grok.Container):
    def __init__(self, name, id=None):
        super(GenericContainer, self).__init__()
        self.name = name
        self.id = id
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

    def delete(self,id):
        self.item_order.pop(self.item_order.index(int(id)))

    def add_item(self,item):
        self[unicode(self.item_count)] = item
        self.item_order.append(self.item_count)
        self.item_count += 1

    def max(self):
        if self.items() is not None:
            return self.items()[-1]
    
    def min(self):
        if self.items is not None:
            return self.items()[0]
            

class Index(grok.View):
    def update(self):
        pdb.set_trace()
    
    #def app(self):
    #    return get_application(self.context)

class ViewContent(grok.Viewlet):
    grok.viewletmanager(MainContent)
    grok.order(0)

class Delete(grok.View):
    grok.template('index')
    def update(self,id=None):
        if id is not None:
            self.context.delete(id)
        self.redirect(self.url(get_application(self.context)))

class DeleteView(grok.Viewlet):
    grok.viewletmanager(MainContent)
    grok.order(1)

def get_application(context):
    obj = context
    while not isinstance(obj, grok.Application):
        obj = obj.__parent__
    return obj
