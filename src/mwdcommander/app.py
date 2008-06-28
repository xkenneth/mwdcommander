### GROK ###
import grok

### GENERIC ###
import os

### KSS ###
from megrok.kss import KSSActions

### ZOPE ###
from zope.component import getMultiAdapter
from zope.interface import Interface


### APP ###
from viewletmanagers import Navigation, MainContent
from boilerplate import GenericContainer, get_application
from pipetallylog import PipeTallyLog, IPipeTallyLog


### KSS ###
class AppKSS(KSSActions):

    def welcome(self):
        core = self.getCommandSet('core')
        core.replaceHTML('#click-me', '<p>ME GROK KISSED !</p>')

### MWD ###
class MWDCommander(grok.Application, grok.Container):
    pass

### VIEWS ###

class Index(grok.View):
    grok.context(MWDCommander)
    pass # see app_templates/index.pt

class PipeTally(grok.View):
    grok.template('index')

### VIEWLETS ###
class Welcome(grok.Viewlet):
    grok.viewletmanager(MainContent)
    grok.view(Index)

### Pipe Tally Log Management ###
class AddPipeTallyLog(grok.Viewlet):
    grok.viewletmanager(MainContent)
    grok.order(0)
    grok.view(PipeTally)
    
    def update(self):
        self.form = getMultiAdapter((self.context,self.request), name=u'addpipetallylogform')
        self.form.update_form()
        
    def render(self):
        return self.form.render()

class AddPipeTallyLogForm(grok.AddForm):
    grok.context(MWDCommander)
    form_fields = grok.AutoFields(PipeTallyLog)
    template = grok.PageTemplate(filename=os.path.join('app_templates','edit_form.pt'))
    
    @grok.action('Add pipetally')
    def add(self, **data):
        obj = PipeTallyLog(**data)
        
        #see if the container exists
        try:
            self.context['pipetallies']
        except:
            self.context['pipetallies'] = GenericContainer()
            
        #add the tally log
        self.context['pipetallies'][obj.name] = obj
    
        app = get_application(self.context)
        self.redirect(self.url(app,'pipetallies'))
        
            
        



