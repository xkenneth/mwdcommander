import grok
import os
import pdb

### APP ###
from viewletmanagers import MainContent

### ZOPE ###
from zope.component import getMultiAdapter
from zope.interface import Interface
from zope.schema import TextLine
from persistent.list import PersistentList

grok.templatedir('app_templates')

class IPipeTallyLog(Interface):
    name = TextLine(title=u"Name:")

class PipeTallyLog(grok.Container):

    grok.implements(IPipeTallyLog)

    def __init__(self, name , id):
	super(PipeTallyLog, self).__init__()
        self.name = name
        self.id = id
	self.tally_count = 0
	self.tally_order = PersistentList()

class Index(grok.View):
    pass

class Edit(grok.View):
    grok.template('index')
    pass

class ViewPipeTallyLog(grok.Viewlet):
    grok.viewletmanager(MainContent)
    grok.order(0)
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
        

    

            
