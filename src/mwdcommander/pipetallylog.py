import grok
import os
import pdb

### APP ###
from viewletmanagers import MainContent
from pipetally import PipeTally, IPipeTally
from boilerplate import get_application, GenericContainer

### ZOPE ###
from zope.component import getMultiAdapter
from zope.interface import Interface
from zope.schema import TextLine
from persistent.list import PersistentList

grok.templatedir('app_templates')

class IPipeTallyLog(Interface):
    name = TextLine(title=u"Name:")

class PipeTallyLog(GenericContainer):
    grok.implements(IPipeTallyLog)

class Index(grok.View):
    pass

class Edit(grok.View):
    grok.template('index')
    pass

class ViewPipeTallyLog(grok.Viewlet):
    grok.viewletmanager(MainContent)
    grok.order(1)
    grok.view(Index)
    
class EditPipeTallyLog(grok.Viewlet):
    grok.viewletmanager(MainContent)
    grok.order(0)
    grok.view(Edit)
    
    def update(self):
        self.form = getMultiAdapter((self.context, self.request), name=u'editpipetallylogform')
        self.form.update_form()
    
    def render(self):
        return self.form.render()

class EditPipeTallyLogForm(grok.EditForm):
    form_fields = grok.AutoFields(PipeTallyLog)
    template = grok.PageTemplate(filename=os.path.join('app_templates','edit_form.pt'))

### PIPE TALLY ###
#VIEWLETS
class AddPipeTally(grok.Viewlet):
    grok.viewletmanager(MainContent)
    grok.order(0)
    grok.view(Index)
    grok.context(PipeTallyLog)
    
    def update(self):
        self.form = getMultiAdapter((self.context, self.request), name=u'addpipetallyform')
        self.form.update_form()

    def render(self):
        return self.form.render()

class AddPipeTallyForm(grok.AddForm):
    grok.context(PipeTallyLog)
    form_fields = grok.AutoFields(PipeTally)
    template = grok.PageTemplate(filename=os.path.join('app_templates','edit_form.pt'))

    @grok.action('Add pipetally')
    def add(self, **data):
        data['id'] = self.context.item_count
        obj = PipeTally(**data)

        self.context[unicode(self.context.item_count)] = obj
        self.context.item_order.append(self.context.item_count)
        self.context.item_count += 1
        
        app = get_application(self.context)
        self.redirect(self.url('index'))
        

    

            
