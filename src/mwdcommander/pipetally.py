import grok
import os
import pdb

### UTILS ###
import mx.DateTime
import datetime

### ZOPE ###
from persistent.mapping import PersistentMapping
from persistent.list import PersistentList
from zope.component import getMultiAdapter
from zope.interface import Interface
from zope.schema import TextLine
import zope.schema

### APP ###
from viewletmanagers import MainContent
from boilerplate import get_application

#shared templates
grok.templatedir('app_templates')

### INTERFACE ###
class IPipeTally(Interface):
    length = TextLine(title=u"Length:",default=u'30')

### MODEL ###
class PipeTally(grok.Model):
    grok.implements(IPipeTally)

    def __init__(self, length, id):
        self.length = float(length)
        self.id = int(id)

### VIEWS ###
class Index(grok.View):
    pass

class Edit(grok.View):
    grok.template('index')

class Delete(grok.View):
    grok.template('index')

    def update(self,id=None):
        if id is not None:
            self.context.__parent__.delete(id)
            app = get_application(self.context)
            self.redirect(self.url(self.context.__parent__))



class EditPipeTally(grok.Viewlet):
    grok.viewletmanager(MainContent)
    grok.order(0)
    grok.view(Edit)
    grok.context(PipeTally)
    def update(self):
        self.form = getMultiAdapter((self.context, self.request), name=u'editpipetallyform')
        self.form.update_form()

    def render(self):
        return self.form.render()

class DeletePipeTally(grok.Viewlet):
    grok.viewletmanager(MainContent)
    grok.order(0)
    grok.view(Delete)
    grok.context(PipeTally)

class EditPipeTallyForm(grok.EditForm):
    grok.context(PipeTally)
    form_fields = grok.AutoFields(PipeTally)
    template = grok.PageTemplate(filename=os.path.join('app_templates','edit_form.pt'))

# class PipeTallyList(grok.Viewlet):
#     grok.viewletmanager(MainContent)
#     grok.context(PipeTallyLog)
#     grok.view(Index)
#     grok.order(1)

class PipeTallyView(grok.Viewlet):
    grok.viewletmanager(MainContent)
    grok.context(PipeTally)
    grok.view(Index)
    grok.order(0)

