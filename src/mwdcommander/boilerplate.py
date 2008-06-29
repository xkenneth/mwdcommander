### GROK ###
import grok

grok.templatedir('app_templates')

### BOILERPLATE ###

class GenericContainer(grok.Container):
    def items(self):
        t = []
        for key in self.item_order: t.append(self[unicode(key)])
        return t

class Index(grok.View):
    pass

def get_application(context):
    obj = context
    while not isinstance(obj, grok.Application):
        obj = obj.__parent__
    return obj
