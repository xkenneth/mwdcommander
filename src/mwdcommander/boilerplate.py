### GROK ###
import grok

grok.templatedir('app_templates')

### BOILERPLATE ###

class GenericContainer(grok.Container):
    pass

class Index(grok.View):
    pass

def get_application(context):
    obj = context
    while not isinstance(obj, grok.Application):
        obj = obj.__parent__
    return obj
