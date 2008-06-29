### GROK ###
import grok

### GENERIC ###
import os
import pdb

### KSS ###
from megrok.kss import KSSActions

### ZOPE ###
from zope.component import getMultiAdapter
from zope.interface import Interface

### ZODB ###
from persistent.list import PersistentList

### APP ###
from viewletmanagers import Navigation, MainContent
from boilerplate import GenericContainer, get_application
from pipetallylog import PipeTallyLog, IPipeTallyLog
from comment import Comment, IComment


### KSS ###
class AppKSS(KSSActions):

    def welcome(self):
        core = self.getCommandSet('core')
        core.replaceHTML('#click-me', '<p>ME GROK KISSED !</p>')
    
    def delete_pipe_tally_log(self,logid=None):
        #pdb.set_trace()
        core = self.getCommandSet('core')
        core.replaceHTML('#'+str(logid), '<span/>')
        self.context['pipetallies'].item_order.pop(self.context['pipetallies'].item_order.index(int(logid[1:])))
        
### MWD ###
class MWDCommander(grok.Application, grok.Container):
    pass

### VIEWS ###

class Index(grok.View):
    grok.context(MWDCommander)
    pass # see app_templates/index.pt

class PipeTally(grok.View):
    grok.template('index')

class Comments(grok.View):
    grok.template('index')
    def update(self):
        try:
            self.context['commentslist']
        except KeyError:
            self.context['commentslist'] = GenericContainer('Comments Container',0)

### VIEWLETS ###
class Welcome(grok.Viewlet):
    grok.viewletmanager(MainContent)
    grok.view(Index)

class PipeTallyLogList(grok.Viewlet):
    grok.viewletmanager(MainContent)
    grok.view(PipeTally)
    grok.order(1)

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
        #see if the container exists
        try:
            self.context['pipetallies']
        except:
            self.context['pipetallies'] = GenericContainer('Pipe Tally Container',0)
        
        data['id'] = unicode(self.context['pipetallies'].item_count)

        obj = PipeTallyLog(**data)
            
        #add the tally log
        self.context['pipetallies'].add_item(obj)
        #self.context['pipetallies'][unicode(self.context['pipetallies'].item_count)] = obj
        #self.context['pipetallies'].item_order.append(self.context['pipetallies'].item_count)
        #self.context['pipetallies'].item_count += 1

    
        app = get_application(self.context)
        self.redirect(self.url(app,'pipetallies'))


### Comments Management ###
class AddComment(grok.Viewlet):
    grok.viewletmanager(MainContent)
    grok.order(0)
    grok.view(Comments)
    def update(self):
        self.form = getMultiAdapter((self.context, self.request), name=u'addcommentform')

    def render(self):
        return self.form.render()

class AddCommentForm(grok.AddForm):
    grok.context(MWDCommander)
    form_fields = grok.AutoFields(Comment)
    template = grok.PageTemplate(filename=os.path.join('app_templates','edit_form.pt'))

    @grok.action('Add pipetally')
    def add(self, **data):
        data['id'] = unicode(self.context['commentslist'].item_count)
        
        obj = Comment(**data)
        
        self.context['commentslist'].add_item(obj)

        app = get_application(self.context)
        self.redirect(self.url(app,'comments'))
        
        

        

        
            
        



